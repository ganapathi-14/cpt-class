import os 
folder=input("enter folder name to create : ")
if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"Folder ' {folder} ' created")
else:
    print("folder already exist")