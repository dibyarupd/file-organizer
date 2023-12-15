# /usr/bin/env python3
from time import sleep
from pathlib import Path
from watchdog.observers import Observer
from MyHandler import MyHandler

# directory to be observed by watchdog module
source_dir = Path(r"D:\ForProject\Look At Me")

if __name__ == "__main__":
    event_handler = MyHandler()

    observer = Observer()
    observer.schedule(event_handler, str(source_dir), recursive=True)
    observer.start()

    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
