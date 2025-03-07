## Learning AI

## Download YT follow-along Videos

Following Karpathy's NN Zero to Hero

```bash
brew install yt-dlp
yt-dlp -f bestvideo+bestaudio --merge-output-format mp4 -o "%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" --write-thumbnail --write-auto-sub --embed-subs --embed-metadata --embed-thumbnail "https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ"
```

## Dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
poetry init --name ai-no-uta --description "Learning AI" --author "Sayan Naskar" --python ">=3.13" --dependency numpy --dependency pandas --dependency matplotlib --dev-dependency pytest --dev-dependency black --dev-dependency isort --dev-dependency ipykernel -n
# poetry run pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
poetry run python -c "import torch; print(torch.__version__); print(torch.backends.mps.is_available())"
git clone https://github.com/karpathy/nn-zero-to-hero.git
```
