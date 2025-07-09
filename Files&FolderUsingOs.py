import os

#Folder Creation
folder="ASG_Folder"
if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"Folder '{folder}' Created ")
else:
    print(f"Folder '{folder}' already exists.")



#Folder Deletion
import os
file = "DeleteMe.txt"
if os.path.exists(file):
    os.remove(file)
    print(f"File '{file}' deleted.")
else:
    print(f"File '{file}' Not Found")



#FindingSizeOfTheFile
import os
file = "SysModule.py"
if os.path.exists(file):
    size=os.path.getsize(file)
    print(f"'{file}' size:{size} Bytes")
else:
    print(f"File '{file}' Not Found")



#AllFilesInFolder
path = "."
files = os.listdir(path)
print("\nFiles and folders in current directory:")
for f in files:
    print(f)
