with open("File1.txt", "r") as f1, open("File2.txt", "r") as f2:
    data1 = f1.read()
    data2 = f2.read()
    print("Data of File1 : ",data1)
    print("Data of File2 : ",data2)

#By using "with" keyword .we dont close the file. it automatically closes
#2

filenames = ["file1.txt", "file2.txt", "file3.txt"]
for fname in filenames:
    with open(fname, "r") as f:
        content = f.read()
        print(f"Content of {fname}:")
        print(content)
       
