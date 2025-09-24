import requests

url="https://api.github.com/users/mvaibhav1"

response=requests.get(url)
data=response.json()
print("Full data :",data)
print("user :",data["login"])
print("Name :",data["name"])
print("Public Repos :",data["public_repos"])
print("Followers:",data["followers"])