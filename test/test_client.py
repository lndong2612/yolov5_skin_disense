import cv2
import requests


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
fontScale = 0.5
image_h, image_w, _ = im.shape
bbox_thick = int(0.6 * (image_h + image_w) / 600)
bbox_color = (0, 255, 0)
thickness = 2

# Draw bbox on input image
for info in classified['content']:
    xmin = info['xmin']
    ymin = info['ymin']
    xmax = info['xmax']
    ymax = info['ymax']
    c1, c2 = (xmin, ymin), (xmax, ymax)
    score = float(info['score'])
    if score < 0.5:
        pass
    else:
        bbox_mess = '%s - %s' % (info['label'], info['score'])
        t_size = cv2.getTextSize(bbox_mess, 0, fontScale, thickness=bbox_thick // 2)[0]
        c3 = (c1[0] + t_size[0], c1[1] - t_size[1] - 7)
        c4 = (c2[0] - t_size[0], c2[1] + t_size[1] + 7)
        if ymin <= 10:
          cv2.rectangle(im, c2, c4, bbox_color, -1) #filled
          cv2.putText(im, bbox_mess, (c2[0] - t_size[0], c2[1] + t_size[1] + 5), cv2.FONT_HERSHEY_SIMPLEX,
              fontScale, (0, 0, 0), bbox_thick // 2, lineType=cv2.LINE_AA)                
        else:
          cv2.rectangle(im, c1, c3, bbox_color, -1) #filled
          cv2.putText(im, bbox_mess, (c1[0] + 1, c1[1] - 3), cv2.FONT_HERSHEY_SIMPLEX,
                fontScale, (0, 0, 0), bbox_thick // 2, lineType=cv2.LINE_AA)               
        cv2.rectangle(im, c1, c2, bbox_color, thickness)
        
cv2.imshow('Im show', im)
cv2.waitKey(0)