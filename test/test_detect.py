import os
import sys
WORKING_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(WORKING_DIR, "../"))

import requests


# The url of the api endpoint
# url = 'https://tclinic-ai.thinklabs.com.vn/detect_object'
url = 'http://127.0.0.1:8080/detect_object'

# The path of the image file
image_path = "./test/images/skin_disense/zona2.jpg"

# The files for the request
files = {
  "file": (image_path, open(image_path, "rb"), "image/jpeg")
}

# Send the post request and print the response
response = requests.post(url, files=files)
classified = response.json()
print(response.json())
