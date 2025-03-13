import os
import yaml
import subprocess
import openai
from pathlib import Path

# Load Azure OpenAI Configuration
CURR_DIR = Path(__file__).resolve().parent
CONFIG_FILE = CURR_DIR / "config.yaml"

def load_config():
    with open(CONFIG_FILE, "r") as f:
        return yaml.safe_load(f)

config = load_config()

# Set OpenAI API for Azure
openai.api_base = config["endpoint"]
openai.api_key = config["key"]
openai.api_version = config["version"]
DEPLOYMENT_NAME = config["chatDeployment"]

VIDEO_EXTENSIONS = {".mp4", ".mkv", ".avi", ".mov", ".flv"}
REFS_DIR = CURR_DIR / "refs"  # Directory for SRT and markdown reference files
os.makedirs(REFS_DIR, exist_ok=True)  # Create refs directory if it doesn't exist

def extract_subtitles(video_path: Path, output_path: Path):
    """Extract subtitles from video file or generate them using Whisper."""
    video_filename = Path(video_path).stem
    srt_file = output_path / f"{video_filename}.srt"
    
    # Try extracting embedded subtitles with -y flag to avoid prompts
    cmd = ["ffmpeg", "-y", "-i", video_path, "-map", "0:s:0", str(srt_file)]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.DEVNULL)

    if srt_file.exists():
        print(f"Extracted subtitles: {srt_file}")
        return srt_file
    
    # Generate subtitles using Whisper, preventing interactive prompts
    print(f"No subtitles found, transcribing using Whisper: {video_path}")
    whisper_cmd = ["whisper", video_path, "--model", "small", "--language", "en", "--output_format", "srt", "--output_dir", str(output_path)]
    subprocess.run(whisper_cmd, stdin=subprocess.DEVNULL)
    
    # Check if the file was created with the correct name
    if srt_file.exists():
        print(f"Generated subtitles: {srt_file}")
        return srt_file
    
    # Whisper might have used a different naming convention, try to find it
    potential_srt = list(output_path.glob(f"{video_filename}*.srt"))
    if potential_srt:
        print(f"Generated subtitles: {potential_srt[0]}")
        return potential_srt[0]
    
    print(f"Failed to extract/generate subtitles for {video_path}")
    return None

def summarize_with_llm(text):
    """Summarize extracted subtitles using Azure OpenAI with an example format."""
    example_markdown = """
    ## 14. $\\mathbb{R}^n$ as Vectors

    Addition:

    $$
    \\begin{bmatrix} 1 \\\\ 2 \\\\ 3 \\end{bmatrix} +
    \\begin{bmatrix} -2 \\\\ 7 \\\\ -6 \\end{bmatrix} =
    \\begin{bmatrix} -1 \\\\ 9 \\\\ -3 \\end{bmatrix}
    $$

    Scalar multiplication:

    $$
    7 \\times \\begin{bmatrix} 4 \\\\ 0 \\\\ 12 \\end{bmatrix} =
    \\begin{bmatrix} 28 \\\\ 0 \\\\ 84 \\end{bmatrix}
    $$

    Stuck in a plane:
    - In each of the vectors in LHS, the third entry is 3 times the first entry. By any linear combination (multiplication by a scalar or addition), we will always be stuck with vectors having the same property.
    - By geometric analogy, this is called a subspace of $\\mathbb{R}^3$.

    😅 There is no linkage between $\\mathbb{R}^3$ and a plane, which is a term from geometry - other than both being vectors.
    """

    client = openai.AzureOpenAI(
        api_key=config["key"],
        api_version=config["version"],
        azure_endpoint=config["endpoint"]
    )

    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": "Convert this transcript into structured Markdown notes, following the given format. Preserve mathematical notation using LaTeX and Markdown syntax."},
            {"role": "user", "content": f"__For single line latex, USE $ DO NOT USE \\(. Same for multiline latex, use $$, not \\[.__ Here is an example format:\n{example_markdown}\n\nNow process this transcript:\n{text}"}
        ]
    )

    return response.choices[0].message.content


def process_video_files():
    """Process all videos in the current directory."""
    # Path is all folders which have Linear Algebra in the name in the folder ~/Downloads/youtube-downloads/

    paths = [x for x in Path.home().joinpath("Downloads/youtube-downloads/").iterdir() if x.is_dir() and "Linear Algebra" in x.name]
    paths = sorted(paths, key=lambda x: x.name)
    print(f"Found {len(paths)} folders with Linear Algebra in the name.")
    
    for p in paths:
        # create the directory for the playlist
        outDir = REFS_DIR / p.name
        os.makedirs(outDir, exist_ok=True)
        for file in sorted(p.iterdir(), key=lambda x: x.name):
            if Path(file).suffix in VIDEO_EXTENSIONS:
                print(f"Processing: {file}")
                
                # Check if markdown file already exists
                ref_md_filename = outDir / (Path(file).stem + ".md")
                if ref_md_filename.exists():
                    print(f"Markdown file already exists: {ref_md_filename}, skipping...")
                    continue
                    
                srt_path = extract_subtitles(file, outDir)
                if not srt_path:
                    continue
                
                with open(srt_path, "r", encoding="utf-8") as f:
                    transcript = f.read()
                
                markdown_notes = summarize_with_llm(transcript)

                with open(ref_md_filename, "w", encoding="utf-8") as f:
                    f.write(markdown_notes)
                
                print(f"Notes saved: {ref_md_filename}")

if __name__ == "__main__":
    process_video_files()
