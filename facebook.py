import os , shutil
file = open("/home/ironman/Desktop/lists.txt", "r")
data = open("/home/ironman/Desktop/file.txt","w")
for Folder in file:
    files = os.walk(Folder.strip())
    for Folders , SubFolder , Files  in files:
        name = ("Folder is " + str(Folders) + "\nSubfolder is " + str(SubFolder) + "\nFile is " + str(Files) + "\n\n")
        data.write(name)
        for empty in Folders:
            if len(empty)== 0:
                print('empty')
                os.rmdir(empty)
            else:
                pass
        for emptySub in SubFolder:
            if (emptySub)== []:
                print("empty")
                os.rmdir(emptySub)
            else:
                pass
        for emptyFiles in Files:
            if len(emptyFiles)== 0:
                print('empty')
                os.rmdir(emptyFiles)
            else:
                pass
        print(empty)

file.close()
data.close()