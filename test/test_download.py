import requests

url = "http://127.0.0.1:8080/download"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
open("image.jpg", "wb").write(response.content)