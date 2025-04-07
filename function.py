import platform
import re
import subprocess
import os

def open_folder_in_explorer(path):
    if platform.system() == "Windows":
        subprocess.run(["explorer", f'/select,{os.path.normpath(path)}'])
    elif platform.system() == "Darwin":
        subprocess.run(["open", "-R", path])
    else:
        folder = os.path.dirname(path)
        subprocess.run(["xdg-open", path])

def is_valid_filename(filename):
    return bool(re.match(r'^[^\\/:*?"<>|]+$', filename.strip()))