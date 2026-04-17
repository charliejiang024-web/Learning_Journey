import os

TRASH_EXT = (".log", ".tmp", ".bak")

def is_trash(file_path):
    if not os.path.isfile(file_path):
        return False

    filename = os.path.basename(file_path)
    return filename.endswith(TRASH_EXT)