import os
import uuid
import shutil
from app.utils.file_utils import validate_file, ensure_directory

def save_file(file, folder):
    ensure_directory(folder)

    ext = validate_file(file)
    filename = f"{uuid.uuid4()}.{ext}"
    filepath = os.path.join(folder, filename)

    try:
        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise Exception(f"File saving failed: {str(e)}")

    return filepath