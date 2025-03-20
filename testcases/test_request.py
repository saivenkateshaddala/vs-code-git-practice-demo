import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print(response.status_code)  # 200
print(response.json())       # JSON data of the post
