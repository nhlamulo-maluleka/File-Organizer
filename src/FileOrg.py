import pathlib
import time
import calendar
import os

# File Directories
directories = [
    os.path.join(os.environ['USERPROFILE'], "Downloads"),
    os.path.join(os.environ['USERPROFILE'], "Pictures"),
    os.path.join(os.environ['USERPROFILE'], "Videos"),
    os.path.join(os.environ['USERPROFILE'], "Music"),
    os.path.join(os.environ['USERPROFILE'], "Documents"),
    os.path.join(os.environ['USERPROFILE'], "Applications")
]

# NB: The following list of extensions is not a comprehensive list of all the extensions,
# and as a result, some of your files may not be covered in this list.

# You can download the file and alter the program to cover your preferred extensions.

images = ['jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'png', 'svg', 'gif',
          'webp', 'bmp', 'ico', 'cur', 'tif', 'tiff', 'apng', 'avif']

videos = ['webm', 'mpg', 'mp2', 'mpeg', 'mpe', 'mpv', 'ogg', 'mp4',
          'm4p', 'm4v', 'avi', 'wmv', 'mov', 'qt', 'flv', 'swf', 'avchd']

audio = ['mp3', 'aac', 'ogg', 'flac', 'wav', 'aiff', 'dsd', 'pcm', 'm4a']

documents = ['doc', 'vsd', 'docx', 'html', 'htm', 'odt', 'pdf', 'xls',
             'xlsx', 'ods', 'odp', 'ppt', 'pptx', 'txt', 'epub', 'zip', 'json', 'xml', 'asm', 
             'spec', 'docm', 'toc', 'pkg', 'py', 'pyz', 'pyw', 'java', 'cpp', 'dart', 'css', 
             'xhtml', 'key', 'csv', 'one', 'yaml', 'js', 'jsx', 'ts']

applications = ['exe', 'msi', 'iso', 'ics', 'torrent', 'eml', 'ios']


# This function checks if a [destination directory] exists and if not, it creates it!
def createDir(path, year, pathName):
    if not pathlib.Path(f"{path}\\{year}\\{pathName}").exists():
        pathlib.Path(f"{path}\\{year}\\{pathName}").mkdir(
            exist_ok=True, parents=True)

# This functions moves the files to their respective directories
def moveFile(file):
    # Setting the current localtime
    ltime = time.localtime()

    fileExtension = file.name.split(".")[-1]
    year = ltime.tm_year
    month = calendar.month_name[ltime.tm_mon]
    # newFileName = f"{year}_{month[:3]}_{day}_{file.name}"
    newFileName = f"{file.name}"

    # Places a file in the Pictures Folder
    if fileExtension in images:
        createDir(directories[1], year, month)
        os.replace(file, f"{directories[1]}\\{year}\\{month}\\{newFileName}")

    # Places a file in the Videos Folder
    elif fileExtension in videos:
        createDir(directories[2], year, month)
        os.replace(file, f"{directories[2]}\\{year}\\{month}\\{newFileName}")

    # Places a file in the Music Folder
    elif fileExtension in audio:
        createDir(directories[3], year, month)
        os.replace(file, f"{directories[3]}\\{year}\\{month}\\{newFileName}")

    # Places a file in the Documents Folder
    elif fileExtension in documents:
        createDir(directories[4], year, month)
        os.replace(file, f"{directories[4]}\\{year}\\{month}\\{newFileName}")

    # Places a file in the Applications Folder
    elif fileExtension in applications:
        createDir(directories[5], year, month)
        os.replace(file, f"{directories[5]}\\{year}\\{month}\\{newFileName}")

# [[Main Function Summary]]

# For each directory, check if there are files in that directory,
# And if they are files, move them to their rightful directories,
# But don't touch any folders in the directory.

if __name__ == "__main__":
    while True:
        for dir in directories:
            path = pathlib.Path(dir)
            # Enter a directory and check if there are files in that [root directory] without entering the sub-folders.
            for file in path.iterdir():
                # Check if the file actually exists in the directory
                if os.path.exists(file):
                    # Move the file if it is not a folder
                    if file.is_file():
                        moveFile(file)
                    # else
                    #   It is a folder
