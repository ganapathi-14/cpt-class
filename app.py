with open('File1.txt',"r+") as file :
    file.write("\nAppended data")
    file.seek(0)
    print(file.read())