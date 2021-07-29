import os, sys
from stat import *
import shutil

def walktree(top, callback):
    for f in os.listdir(top):
        if f != "photos":
            pathname = os.path.join(top, f)
            mode = os.stat(pathname)[ST_MODE]

            if S_ISDIR(mode):
                # It's a directory, recurse into it
                walktree(pathname, callback)
            elif S_ISREG(mode):
                # It's a file, call the callback function
                callback(pathname)
            else:
                # Unknown file type, print a message
                print('Skipping %s', pathname)

def visitfile(file):
    if file[-5:] == '.jpeg':
        msg = 'visiting' + file + '\n'
        f.write(msg)

        file_name = file.split("/")[-1]
        new_path = '/home/dj-d/Downloads/Test/photos/' + file_name

        if not os.path.isfile(new_path):
            msg = "Moved: " + new_path + '\n\n'
            f.write(msg)
            
            shutil.move(file, new_path)
        else:
            msg = 'Already exist: ' + new_path + '\n\n'
            f.write(msg)
        

if __name__ == '__main__':
    print('Start')
    f = open('work_video_jpeg.log', 'w')

    walktree(sys.argv[1], visitfile)

    f.close()
    print('Finish')
