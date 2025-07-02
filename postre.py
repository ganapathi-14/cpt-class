import requests
url=requests.get("https://jsonplaceholder.typicode.com/posts/1")
data={
    "title":"Hii Students",
    "body":"Wiprp Geeks",
    "userid":1

}
response=requests.post(url,json=data)
print("Status code: ",response.status_code)
print("response.json: ",response.json())
