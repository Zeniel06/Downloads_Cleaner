import os
import shutil
from pathlib import Path

# Define the Downloads folder
downloads_dir = Path.home() / "Downloads"

# File types and their corresponding folders
file_types = {
    "App": [".exe"],
    "Image": [".jpg", ".jpeg", ".png", ".gif", ".tiff", ".bmp", ".eps"],
    "Code": [".ipynb", ".py", ".js", ".html", ".css", ".php", ".cpp", ".h", ".java", ".ms14", ".m"],
    "Document": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".ogg"],
    "Video": [".mp4", ".avi", ".mov", ".flv", ".wmv", ".mpeg"],
    "Photoshop": [".psd"],
    "Zipped Folders": [".zip"],
}

# Create folders if they don't exist
for folder in file_types:
    (downloads_dir / folder).mkdir(exist_ok=True)

# Move files based on their extension
for file in downloads_dir.iterdir():
    if file.is_file():
        for folder, extensions in file_types.items():
            if file.suffix in extensions:
                shutil.move(str(file), str(downloads_dir / folder / file.name))
                break
