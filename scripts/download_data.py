#!/usr/bin/env python3
"""Download MovieLens dataset"""

import requests
import zipfile
from pathlib import Path

DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)

print("📥 Downloading MovieLens dataset...")

url = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
zip_path = DATA_DIR / "movielens.zip"

response = requests.get(url, stream=True)
with open(zip_path, 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)

print("✓ Download complete")
print("📂 Extracting files...")

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(DATA_DIR)

print("✓ Setup complete!")
