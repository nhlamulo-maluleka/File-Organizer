import pathlib
import mimetypes
import time
import calendar
import os

mimetype = mimetypes.MimeTypes()
ltime = time.localtime()

# File Directors
directories = [
    os.path.join(os.environ['USERPROFILE'], "Downloads"),
    os.path.join(os.environ['USERPROFILE'], "Pictures"),
    os.path.join(os.environ['USERPROFILE'], "Videos"),
    os.path.join(os.environ['USERPROFILE'], "Music"),
    os.path.join(os.environ['USERPROFILE'], "Documents"),
    os.path.join(os.environ['USERPROFILE'], "Applications")
]

images = ['jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'png', 'svg', 'gif',
          'webp', 'bmp', 'ico', 'cur', 'tif', 'tiff', 'apng', 'avif']
videos = ['webm', 'mpg', 'mp2', 'mpeg', 'mpe', 'mpv', 'ogg', 'mp4',
          'm4p', 'm4v', 'avi', 'wmv', 'mov', 'qt', 'flv', 'swf', 'avchd']
audio = ['mp3', 'aac', 'ogg', 'flac', 'wav', 'aiff', 'dsd', 'pcm', 'm4a']
documents = ['doc', 'vsd', 'docx', 'html', 'htm', 'odt', 'pdf', 'xls',
             'xlsx', 'ods', 'ppt', 'pptx', 'txt', 'epub', 'zip', 'json', 'xml', 'asm']
applications = ['exe', 'msi', 'iso', 'ics', 'torrent', 'eml']


def createDir(path, year, pathName):
    if not pathlib.Path(f"{path}\\{year}\\{pathName}").exists():
        pathlib.Path(f"{path}\\{year}\\{pathName}").mkdir(
            exist_ok=True, parents=True)


def moveFile(file):
    fileExtension = file.name.split(".")[-1]
    day = ltime.tm_mday
    year = ltime.tm_year
    month = calendar.month_name[ltime.tm_mon]
    # newFileName = f"{year}_{month[:3]}_{day}_{file.name}"
    newFileName = f"{file.name}"

    if fileExtension in images:
        createDir(directories[1], year, month)
        os.replace(file, f"{directories[1]}\\{year}\\{month}\\{newFileName}")

    elif fileExtension in videos:
        createDir(directories[2], year, month)
        os.replace(file, f"{directories[2]}\\{year}\\{month}\\{newFileName}")

    elif fileExtension in audio:
        createDir(directories[3], year, month)
        os.replace(file, f"{directories[3]}\\{year}\\{month}\\{newFileName}")

    elif fileExtension in documents:
        createDir(directories[4], year, month)
        os.replace(file, f"{directories[4]}\\{year}\\{month}\\{newFileName}")

    elif fileExtension in applications:
        createDir(directories[5], year, month)
        os.replace(file, f"{directories[5]}\\{year}\\{month}\\{newFileName}")


if __name__ == "__main__":
    while True:
        for dir in directories:
            path = pathlib.Path(dir)
            for file in path.iterdir():
                if os.path.exists(file):
                    if file.is_file():
                        moveFile(file)
