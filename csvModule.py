import csv
with open ("people.csv","w",newline="") as file:
 writer=csv.writer(file)
 writer.writerow(["name","age"])
 for _ in range(2):
  name=input("Enter Name : ")
  age=int(input("Enter age"))
  writer.writerow([name,age])
print("Data written on csv file")

with open ("people.csv","r",newline="") as file:
 reader=csv.reader(file)
 for row in reader:
  print(row)