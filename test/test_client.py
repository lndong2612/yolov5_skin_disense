import cv2
import requests
from utils.plots import draw_bbox

# The url of the api endpoint
url = "http://127.0.0.1:8080/detect_object"

# The path of the image file
image_path = "./test/images/skin_disense/zona.jpg"

# The headers for the request
headers = {
  "accept": "application/json",
  "apikey": "API0KEY0"
}

# The files for the request
files = {
  "file": (image_path, open(image_path, "rb"), "image/jpeg")
}

# Send the post request and print the response
response = requests.post(url, headers=headers, files=files)
classified = response.json()
print(response.json())

# Load image
im = cv2.imread(image_path)
im_show = draw_bbox(im, classified)
cv2.imshow('Im show', im_show)
cv2.waitKey(0)