from pathlib import WindowsPath
from extensions import extension_paths
from datetime import datetime
import shutil
from watchdog.events import FileSystemEventHandler

# source directory
source_dir = WindowsPath(r"D:\ForProject\Look At Me")
# destination directory
destination_dir = WindowsPath(r"D:\ForProject\Place Here")


# adding Year and Month in file path
def add_date_to_file(path: WindowsPath) -> WindowsPath:
    path = path / f'{datetime.now().year}' / f'{datetime.now().month}'
    path.mkdir(parents=True, exist_ok=True)
    return path


# renaming file name to destination directory
def rename_file(source_path: WindowsPath, destination_path: WindowsPath) -> WindowsPath:
    temp = destination_path / source_path.name
    if temp.exists():
        inc = 0
        while temp.exists():
            inc += 1
            temp = destination_path / f'{source_path.stem}({inc}){source_path.suffix.lower()}'
        return temp
    else:
        return temp


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file in source_dir.rglob('*'):
            if file.is_file():
                if file.suffix.lower() in extension_paths:
                    destination_path = destination_dir / extension_paths[file.suffix.lower()]
                else:
                    destination_path = destination_dir / extension_paths['noname']
                destination_path = add_date_to_file(destination_path)
                destination_path = rename_file(file, destination_path)
                try:
                    # used to move/rename a file from one path to another path
                    shutil.move(str(file), str(destination_path))
                except (Exception,):
                    pass
