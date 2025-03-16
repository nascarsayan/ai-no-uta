from pathlib import Path
import re
import subprocess
import shutil
import yaml
import argparse
from typing import List, Tuple, Dict, Any
from manim import (
    Scene, MathTex, Write, Transform, FadeOut, UP, RIGHT, tempconfig
)

# Define paths
curr_file = Path(__file__).resolve()
cwd = curr_file.parent
default_input_dir = (cwd / "../assets").resolve()
default_output_dir = cwd / "media/videos/board_scenes/480p15/"
default_destination = default_input_dir

def parse_markdown(filename: Path) -> Tuple[Dict[str, Any], List[List[str]]]:
    """ Parses the markdown file to extract frontmatter config and step-wise LaTeX matrices. """
    with open(filename, "r", encoding="utf-8") as f:
        content: str = f.read()
    
    # Extract frontmatter
    frontmatter_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    
    if not frontmatter_match:
        raise ValueError(f"No frontmatter found in markdown file: {filename}")
    
    # Parse YAML frontmatter
    frontmatter_yaml = frontmatter_match.group(1)
    cfg = yaml.safe_load(frontmatter_yaml)
    
    # Extract content after frontmatter
    content = content[frontmatter_match.end():]
    
    # Split steps based on "### Step"
    steps: List[str] = re.split(r"### Step \d+", content)
    steps = [step for step in steps if step]

    # Get the number of blocks from frontmatter
    num_blocks = len(cfg.get("blocks", []))
    
    extracted_steps: List[List[str]] = []
    for step in steps:
        # Extract all LaTeX blocks in each step
        latex_blocks: List[str] = re.findall(r"\$\$(.*?)\$\$", step, re.DOTALL)
        
        # Ensure we have the right number of blocks
        if len(latex_blocks) == num_blocks:
            extracted_steps.append(latex_blocks)
        else:
            print(f"Warning: Expected {num_blocks} LaTeX blocks, found {len(latex_blocks)} in step for {filename}")
    
    return cfg, extracted_steps

class BoardScene(Scene):
    def __init__(self, markdown_file=None, **kwargs):
        super().__init__(**kwargs)
        self.markdown_file = markdown_file
        
    def construct(self) -> None:
        if not self.markdown_file:
            raise ValueError("No markdown file specified for BoardScene")
            
        # Read the markdown file and extract config and steps
        cfg, steps = parse_markdown(self.markdown_file)
        
        # Get font size from config or use default
        font_size = cfg.get("font_size", 40)
        
        # Get block configurations
        blocks_config = cfg.get("blocks", [])
        
        # Check if we have blocks defined
        if not blocks_config:
            raise ValueError(f"No blocks defined in frontmatter of {self.markdown_file}")
        
        # Initial objects dictionary to store references
        objects = {}
        
        # Create initial objects for each block
        for i, block_config in enumerate(blocks_config):
            name = block_config.get("name")
            pos = block_config.get("position", [0, 0])
            
            # Convert position to Manim coordinates (y, x)
            position = UP * pos[0] + RIGHT * pos[1]
            
            # Create and position the object
            obj = MathTex(steps[0][i], font_size=font_size).move_to(position)
            objects[name] = {
                "object": obj,
                "position": position
            }
            
            # Write initial objects
            self.play(Write(obj))
        
        self.wait(2)
        
        # Process each step in sequence
        for step in steps[1:]:
            # Update each block with new content
            for i, block_config in enumerate(blocks_config):
                name = block_config.get("name")
                position = objects[name]["position"]
                
                new_obj = MathTex(step[i], font_size=font_size).move_to(position)
                
                # Transform the object
                self.play(Transform(objects[name]["object"], new_obj))
                self.wait(1)
            
            self.wait(1)
        
        # Fade out all objects
        self.play(FadeOut(*[objects[name]["object"] for name in objects]))

def create_gif_from_video(video_path: Path, gif_path: Path) -> bool:
    """Convert MP4 to GIF using FFmpeg.
    
    Args:
        video_path: Path to the source MP4 file
        gif_path: Path where the GIF will be saved
        
    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        subprocess.run([
            "ffmpeg", "-y", "-i", str(video_path), 
            "-vf", "fps=15,scale=640:-1:flags=lanczos", 
            "-c:v", "gif", str(gif_path)
        ], check=True)
        print(f"Converted {video_path.name} to GIF: {gif_path}")
        return True
    except subprocess.CalledProcessError:
        print(f"FFmpeg failed converting {video_path.name} to GIF.")
        return False

def process_markdown_file(markdown_file: Path, output_dir: Path, destination: Path) -> bool:
    """Process a single markdown file to create video and gif."""
    try:
        output_name = markdown_file.stem
        print(f"Processing {markdown_file.name}...")
        
        # Check if output files already exist
        video_path_dest = destination / f"{output_name}.mp4"
        gif_path_dest = destination / f"{output_name}.gif"
        
        if video_path_dest.exists() and gif_path_dest.exists():
            print(f"Skipping {markdown_file.name} - both video and GIF already exist in {destination}")
            return True
        elif video_path_dest.exists():
            print(f"Found existing video for {markdown_file.name}, only generating GIF")
            # Skip to GIF conversion but use existing video
            if create_gif_from_video(video_path_dest, gif_path_dest):
                return True
            else:
                print(f"Failed to create GIF for {markdown_file.name} from existing video.")
                return True  # Still return True as this is not a critical error
        
        # Set manim configuration for this file
        with tempconfig({
            "output_file": output_name,
            "media_dir": cwd / "media",  # Use a consistent media directory
            "quality": "low_quality",
            "preview": False,
        }):
            # Create and render the scene
            scene = BoardScene(markdown_file=markdown_file)
            scene.render()
        
        # Find the output video by searching for it recursively in the media directory
        # The error log shows the actual path where the file is created
        media_dir = cwd / "media"
        found_videos = list(media_dir.glob(f"**/{output_name}.mp4"))
        
        video_path = None
        if found_videos:
            # Use the most recently created video if multiple are found
            video_path = max(found_videos, key=lambda p: p.stat().st_mtime)
            print(f"Found output video at: {video_path}")
        else:
            print(f"Could not find output video for {markdown_file.name}.")
            print(f"Searched recursively in {media_dir}")
            return False
            
        # Create destination if it doesn't exist
        destination.mkdir(parents=True, exist_ok=True)
        
        # Copy MP4 to destination
        shutil.copy(video_path, destination)
        print(f"Copied {video_path.name} to {destination}")
        
        # Convert MP4 to GIF using the new function
        create_gif_from_video(video_path_dest, gif_path_dest)
        return True
            
    except Exception as e:
        print(f"Error processing {markdown_file.name}: {e}")
    
    return False

def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(description="Process markdown files to create math board animations")
    parser.add_argument("--input-dir", type=str, default=str(default_input_dir),
                        help="Directory containing markdown files to process")
    parser.add_argument("--output-dir", type=str, default=str(default_output_dir),
                        help="Directory for video output")
    parser.add_argument("--destination", type=str, default=str(default_destination),
                        help="Destination directory for final videos and GIFs")
    parser.add_argument("--file", type=str, help="Process a specific markdown file instead of the entire directory")
    
    args = parser.parse_args()
    
    # Convert paths
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    destination = Path(args.destination)
    
    # Create output directories if they don't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Process files
    success_count = 0
    failure_count = 0
    
    if args.file:
        # Process a single specified file
        markdown_file = Path(args.file)
        if not markdown_file.exists():
            print(f"File not found: {markdown_file}")
            return
            
        if process_markdown_file(markdown_file, output_dir, destination):
            success_count += 1
        else:
            failure_count += 1
    else:
        # Process all markdown files in the input directory
        if not input_dir.exists():
            print(f"Input directory not found: {input_dir}")
            print(f"Creating directory: {input_dir}")
            input_dir.mkdir(parents=True, exist_ok=True)
            print(f"Please add markdown files to {input_dir} and run the script again.")
            return
            
        markdown_files = list(input_dir.glob("*.md"))
        if not markdown_files:
            print(f"No markdown files found in {input_dir}")
            return
            
        print(f"Found {len(markdown_files)} markdown files to process.")
        
        for markdown_file in markdown_files:
            if process_markdown_file(markdown_file, output_dir, destination):
                success_count += 1
            else:
                failure_count += 1
    
    # Print summary
    print("\nProcessing complete!")
    print(f"Successfully processed: {success_count}")
    print(f"Failed to process: {failure_count}")

if __name__ == "__main__":
    main()