from stat import *
import argparse
import os, sys
import shutil

def walktree(source, dest, file_type, callback):
    for f in os.listdir(source):
        pathname = os.path.join(source, f)
        mode = os.stat(pathname)[ST_MODE]

        if S_ISDIR(mode):
            # It's a directory, recurse into it
            walktree(pathname, dest, file_type, callback)
        elif S_ISREG(mode):
            # It's a file, call the callback function
            callback(pathname, dest, file_type)
        else:
            # Unknown file type, print a message
            print('Skipping %s', pathname)

def visitfile(file, dest, file_type):
    file_type_len = len(file_type)

    if file[-file_type_len:] == file_type:
        f.write('visiting' + file + '\n')

        file_name = file.split("/")[-1]
        new_path = dest + '/' + file_name

        if not os.path.isfile(new_path):
            f.write("Moved: " + new_path + '\n\n')
            
            shutil.move(file, new_path)
        else:
            f.write('Already exist: ' + new_path + '\n\n')
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        '--source', '-s',
        dest='source',
        required=True,
        type=str,
        help=''
    )

    parser.add_argument(
        '--destination', '-d',
        dest='dest',
        required=True,
        type=str,
        help=''
    )

    parser.add_argument(
        '--file-type', '-t',
        dest='file_type',
        required=True,
        help=''
    )

    parser.add_argument(
        '--log-file', '-l',
        dest='log_file',
        required=True,
        type=str,
        help=''
    )

    args = parser.parse_args()

    print('Start')

    f = open(args.log_file, 'w')

    file_type = '.' + args.file_type
    walktree(args.source, args.dest, file_type, visitfile)

    f.close()
    print('Finish')
