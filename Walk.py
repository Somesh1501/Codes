#!/bin/bash/venv
import os , shutil, send2trash
x = input("Enter the path of Directory\n")
sub =  open("/home/ironman/Pictures/SUb.txt","w")
file = open("/home/ironman/Pictures/Files.txt", "w")

for FolderName , SubFolders , FileNames in os.walk(x):
    print("Current Folder is " + FolderName)
    for SubFolder in SubFolders:
        sub.write("Subfolders in " + FolderName + " is " + SubFolder + "\n\n")

    for FileName in FileNames:
        file.write("File in " + SubFolder + " is " + FileName +"\n\n")

sub.close()
file.close()
