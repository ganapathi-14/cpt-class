with open('File1.txt', "r+") as file:
  content=file.read()
  file.seek(10)
  file.write("Modification done here")