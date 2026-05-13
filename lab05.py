import os
import sys
import pathlib
import zipfile

dirName = input("Enter Directory name to backup: ")

if not os.path.isdir(dirName):
    print("Directory", dirName, "doesn't exists")
    sys.exit(0)

curDir = pathlib.Path(dirName)

with zipfile.ZipFile("myZip.zip", mode="w") as archive:
    for file_path in curDir.rglob("*"):
        print(file_path)
        archive.write(file_path)

if os.path.isfile("myZip.zip"):
    print("Archive myZip.zip created successfully")
else:
    print("Error in creating zip archive")