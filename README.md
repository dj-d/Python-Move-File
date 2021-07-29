# Python-Move-File

Script to move a certain type of files placed in nested folders, into a single folder

## Commands

| Command                | Description               | Example               |
| ---------------------- | ------------------------- | --------------------- |
| __--source / -s__      | Path source folder        | /source/path          |
| __--destination / -d__ | Path destination folder   | /destination/pah      |
| __--file-type / -t__   | File extension            | mp3 / jpg / mkv / ... |
| __--log-file / -l__    | Path and name of log file | path/log/file.log     |

## Example

```
python3 main.py --source /path/source/folder --dest /path/destination/folder -t mp4 -l /path/log/file/mp4_move.log
```