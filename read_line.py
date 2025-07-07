
with open('File1.txt', "r+") as file:
    lines=file.readlines()
    l=len(lines)
    print("List of lines : ",l) #no.of lines
    

with open('File1.txt', "r+") as file:
    lines=file.readlines()
for line in lines:
      print(line.strip()) #removes \n and prints all lines
      
with open("File1.txt", "r") as file:
    content = file.read()
    print(content)  # Outputs all characters in the file

    
with open("File1.txt", "r") as file:
    for line in file:
        for char in line:
            print(char) # Outputs all characters in the file

with open("File1.txt", "r") as file:
    separate_lines=[line.strip() for line in file.readlines()]
    print(separate_lines)


#close

file = open('File1.txt', 'r')
# Check if file is closed (should be False)
print(file.closed)  # Output: False
# Close the file
file.close()
# Check if file is closed (should be True)
print(file.closed)  # Output: True
