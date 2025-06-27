import os
import shutil
import logging

SOURCE_DIR = "/path/to/source"
DEST_DIR = "/path/to/destination"

EXT_MAP = {
    "images": ['.jpg', '.jpeg', '.png', '.gif'],
    "documents": ['.pdf', '.docx', '.txt'],
    "scripts": ['.py', '.sh', '.bat'],
    "archives": ['.zip', '.rar', '.tar.gz'],
    "videos": ['.mp4', '.mkv']
}

logging.basicConfig(filename="file_organizer.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def organize_files():
    for filename in os.listdir(SOURCE_DIR):
        src_path = os.path.join(SOURCE_DIR, filename)
        if os.path.isfile(src_path):
            ext = os.path.splitext(filename)[1].lower()
            moved = False
            for category, extensions in EXT_MAP.items():
                if ext in extensions:
                    dest_path = os.path.join(DEST_DIR, category)
                    os.makedirs(dest_path, exist_ok=True)
                    shutil.move(src_path, os.path.join(dest_path, filename))
                    logging.info(f"Moved {filename} to {category}/")
                    moved = True
                    break
            if not moved:
                logging.warning(f"Uncategorized file: {filename}")

organize_files()
