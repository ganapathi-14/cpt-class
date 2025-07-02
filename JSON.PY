#1
import json
name=input("Enter Name : ")
age=int(input("Enter age : "))
data={"name": name, "age": age}
stringify_json=json.dumps(data)
print("Serialized data of JSON " ,stringify_json)

#2
name=input("Enter Name : ")
age=int(input("Enter age : "))
user ={"name": name, "age": age}
with open("user.json","w") as f:
    json.dump(user,f )
print("\nData Written to json folder")

with open("user.json","r") as f:
    loaded=json.load(f)
    print("\nRead from file : ",loaded)
