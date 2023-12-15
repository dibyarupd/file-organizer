# file-organizer
File Organizer used to move files from one folder of different types to specified folders, created using python.

This project will help you to organize your files present in a specific directory in a destination directory. The only changes you need to make in the code are elaborated as follows.

In FileOrganizer.py, change the following Path object.
```
source_dir = Path(r"path_of_the_source_directory")
```

In MyHandler.py, change the following Path objects,
```
source_dir = Path(r"path_of_the_source_directory")
destination_dir = Path(r"path_of_the_destination_directory")
```

Also this python code is only for Windows operating system. But with a little debugging, you can make it run in your OS as well.
Cheers!
