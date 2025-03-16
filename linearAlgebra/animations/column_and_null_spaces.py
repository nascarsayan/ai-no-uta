from pathlib import Path
import re
import subprocess
import shutil
from typing import List, Tuple
from manim import (
    Scene, MathTex, Write, Transform, FadeOut, UP, LEFT, RIGHT, DOWN
)

# Define paths
curr_file = Path(__file__).resolve()
cwd = curr_file.parent
MARKDOWN_FILE = cwd / "column_and_null_spaces_steps.md"
output_dir = cwd / "media/videos/column_and_null_spaces/480p15/"
destination = cwd / "../assets"

def main():
    # Run Manim command
    subprocess.run(["manim", "-pql", str(curr_file), "ColumnAndNullSpace"], check=True)

    # Find the latest generated video file
    try:
        files = list(output_dir.glob("*.mp4"))
        if files:
            latest_video = max(files, key=lambda f: f.stat().st_mtime)
            video_path = latest_video
            gif_path = destination / latest_video.with_suffix(".gif").name

            # Copy MP4 to destination
            shutil.copy(video_path, destination)
            print(f"Copied {video_path.name} to {destination}")

            # Convert MP4 to GIF using FFmpeg (ignore errors)
            try:
                subprocess.run([
                    "ffmpeg", "-i", str(video_path), "-vf", "fps=15,scale=640:-1:flags=lanczos", "-c:v", "gif", str(gif_path)
                ], check=True)
                print(f"Converted {video_path.name} to GIF: {gif_path}")
            except subprocess.CalledProcessError:
                print("FFmpeg failed, skipping GIF conversion.")

        else:
            print(f"No video files found in {output_dir}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()



def parse_markdown(filename: Path) -> List[Tuple[str, str, str]]:
    """ Parses the markdown file to extract step-wise LaTeX matrices. """
    with open(filename, "r", encoding="utf-8") as f:
        content: str = f.read()

    # Split steps based on "### Step"
    steps: List[str] = re.split(r"### Step \d+", content)
    steps = [step for step in steps if step]

    extracted_steps: List[Tuple[str, str, str]] = []
    for step in steps:
        # Extract all LaTeX blocks in each step
        latex_blocks: List[str] = re.findall(r"\$\$(.*?)\$\$", step, re.DOTALL)
        if len(latex_blocks) == 3:  # Ensure correct number of entries
            extracted_steps.append((latex_blocks[0], latex_blocks[1], latex_blocks[2]))

    return extracted_steps

class ColumnAndNullSpace(Scene):
    def construct(self) -> None:
        # Read the markdown file and extract steps
        steps: List[Tuple[str, str, str]] = parse_markdown(MARKDOWN_FILE)
        font_size: int = 40

        # Positions for elements
        matrix_pos = UP * 2.2 + LEFT * 3.5  # Move matrix slightly left
        r_pos = DOWN * 1 + LEFT * 5.0   # Keep R more visible
        n_pos = DOWN * 1 + RIGHT * 1.5  # Move N further left to prevent cutoff

        # Initial Step (Step 1)
        matrix_obj = MathTex(steps[0][0], font_size=font_size).move_to(matrix_pos)
        r_obj = MathTex(steps[0][1], font_size=font_size).move_to(r_pos)
        n_obj = MathTex(steps[0][2], font_size=font_size).move_to(n_pos)

        self.play(Write(matrix_obj), Write(r_obj), Write(n_obj))
        self.wait(2)

        # Process each step in sequence
        for step in steps[1:]:
            new_matrix = MathTex(step[0], font_size=font_size).move_to(matrix_pos)
            new_r = MathTex(step[1], font_size=font_size).move_to(r_pos)
            new_n = MathTex(step[2], font_size=font_size).move_to(n_pos)

            # Transform elements one by one
            self.play(Transform(matrix_obj, new_matrix))
            self.wait(1)
            self.play(Transform(r_obj, new_r))
            self.wait(1)
            self.play(Transform(n_obj, new_n))
            self.wait(2)

        self.play(FadeOut(matrix_obj, r_obj, n_obj))
