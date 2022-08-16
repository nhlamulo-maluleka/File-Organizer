from time import sleep
import pathlib
import os
from FileOrganizer import directories, moveFile, visitDirectory

# [[Main Function Summary]]

# For each directory, check if there are files in that directory,
# And if they are files, move them to their rightful directories,

if __name__ == "__main__":
    while True:
        for dir in directories:
            path = pathlib.Path(visitDirectory(dir))
            # Enter a directory and check if there are files in that [root directory] without entering the sub-folders.
            for file in path.iterdir():
                # Check if the file actually exists in the directory
                if os.path.exists(file):
                    # Move the file if it is not a folder
                    if file.is_file():
                        moveFile(file)
                    # else
                    #   It is a folder
        sleep(10)
