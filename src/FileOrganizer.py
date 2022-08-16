import pathlib
import calendar
import os
import json
from time import localtime

# NB: The list of extensions provided is not a comprehensive list of all the extensions,
# and as a result, you may edit the json file provided to add your desired extensions.
# BUT DON'T CHANGE THE STRUCTURE OF THE JSON FILE!!

with open('./extensions.json') as listFile:
    config = json.load(listFile)
    images = config["extensions"]['images']
    videos = config["extensions"]['videos']
    music = config["extensions"]['music']
    documents = config["extensions"]['documents']
    applications = config["extensions"]['applications']
    directories = config["watch"]
    listFile.close()

# Enter this directory
def visitDirectory(dirName):
    return os.path.join(os.environ['USERPROFILE'], dirName)

# This function checks if a [destination directory] exists and if not, it creates it!
def createDir(targetDir, year, pathName):
    if not pathlib.Path(f"{targetDir}\\{year}\\{pathName}").exists():
        pathlib.Path(f"{targetDir}\\{year}\\{pathName}").mkdir(exist_ok=True, parents=True)

# Placing the file in the correct directory
def replaceFile(file, targetDir, year, month, newFileName):
    createDir(targetDir, year, month)
    os.replace(file, f"{targetDir}\\{year}\\{month}\\{newFileName}")

# Get Target directory
def getTargetDir(extension):
    # Places a file in the Pictures Folder
    if extension in images:
        return visitDirectory("Pictures")

    # Places a file in the Videos Folder
    elif extension in videos:
        return visitDirectory("Videos")

    # Places a file in the Music Folder
    elif extension in music:
        return visitDirectory("Music")
    
    # Places a file in the Documents Folder
    elif extension in documents:
        return visitDirectory("Documents")

    # Places a file in the Applications Folder
    elif extension in applications:
        return visitDirectory("Applications")

# This function moves the files to their respective directories
def moveFile(file):
    fileExtension = str(file.name).split(".")[-1]
    year = localtime().tm_year
    month = calendar.month_name[localtime().tm_mon]
    newFileName = f"{file.name}"
    targetDir = getTargetDir(fileExtension)

    replaceFile(file, targetDir, year, month, newFileName)
