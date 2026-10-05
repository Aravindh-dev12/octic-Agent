"""Publish huggingface_space/ as a Hugging Face Space."""
from __future__ import annotations
import os
from pathlib import Path
from huggingface_hub import HfApi
ROOT=Path(__file__).resolve().parents[1]
SPACE_DIR=ROOT/"huggingface_space"
REPO_ID=os.environ.get("HF_SPACE_ID","Aravindhan11/octic-ai-agent")
TOKEN=os.environ.get("HF_TOKEN")
if not TOKEN: raise SystemExit("HF_TOKEN is required with write access.")
api=HfApi(token=TOKEN)
api.create_repo(repo_id=REPO_ID,repo_type="space",space_sdk="gradio",exist_ok=True)
api.upload_folder(repo_id=REPO_ID,repo_type="space",folder_path=str(SPACE_DIR),commit_message="Publish Octic AI Agent UI",ignore_patterns=["*.pyc","__pycache__/**"])
print(f"Published https://huggingface.co/spaces/{REPO_ID}")