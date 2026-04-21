import os

ALLOWED_EXTENSIONS = {"pdf", "jpg", "jpeg", "png"}

def validate_file(file):
    ext = file.filename.split(".")[-1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError(f"Invalid file type: {ext}")
    return ext


def ensure_directory(path):
    os.makedirs(path, exist_ok=True)