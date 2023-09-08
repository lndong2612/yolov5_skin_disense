# import os
# import sys
# import cv2
# WORKING_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.join(WORKING_DIR, '../'))   
# import logging
# import numpy as np
# from detect import detect_object
# from flask import Flask, request, jsonify, make_response
# from utils.plots import draw_bbox

# app = Flask(__name__)
# app.debug = True
# app.logger.setLevel(logging.DEBUG)


# @app.route('/')
# def index():
#     return '''Detect skin disense object!<hr>
# <form action="/detect_object" method="POST" enctype="multipart/form-data">
# <input type="file" name="file">
# <button>OK</button>
# </form>    
# '''


# @app.route("/detect_object", methods=['POST'])
# def detect_method():
#     try:
#         weight_path = "./weight_init/best.pt" # model path
#         device = '' # cuda device, i.e. 0 or 0,1,2,3 or cpu
#         data = './data/coco.yaml'        
#         file = request.files.get('file')
#         npimg = np.fromfile(file, np.uint8)
#         image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
#         filename = 'photo.jpg'
#         cv2.imwrite(filename, image)
#         classified = detect_object(weight_path, device, data, filename)
#         im_show = draw_bbox(image, classified)
#         cv2.imwrite('skin_disense.jpg', im_show)
#         return '''<img src="skin_disense.jpg" alt="Italian Trulli">'''
    
#     except Exception as e:
#         return jsonify(status_code=400, content={'success':"false",'error': str(e)})

# @app.route("/resources/images/detect.jpg", methods=['GET'])
# def get_image():
#     path_image = "./resources/images/detect.jpg"
#     if not os.path.exists(path_image):
#         return jsonify(message="Không có ảnh"), 400
#     image = cv2.imread(path_image)
#     if image.shape[1] > 3500:
#         encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 45]
#     elif image.shape[1] > 3000:
#         encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 55]
#     elif image.shape[1] > 2000:
#         encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 75]
#     elif image.shape[1] > 1000:
#         encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
#     else:
#         encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 100]
#     image_bytes = cv2.imencode(".jpg", image, encode_param)[1].tobytes()
#     response = make_response(image_bytes)
#     response.headers.set("Content-Type", "image/jpeg")
#     response.headers.set("Content-Disposition", "attachment", filename='test.jpg')
#     return response

# def run_server_api():
#     app.run(host='0.0.0.0', port=8080)

# if __name__ == "__main__":     
#     run_server_api()

# import cv2
# import unicodedata

# image_path = './test/images/zidane.jpg'
# image = cv2.imread(image_path)
# height, width, _ = image.shape
# mess = '\u03A9'
# print(mess)
# fontScale = 0.75
# bbox_thick = int(0.6 * (height + width) / 350)
# bbox_color = (0, 255, 0)
# thickness = 2
# cv2.putText(image, mess, (5, 30), cv2.FONT_HERSHEY_SIMPLEX,
#             fontScale, (0, 255, 0), bbox_thick // 2, lineType=cv2.LINE_AA)
# cv2.imshow('IMG', image)
# cv2.waitKey(0)

from PIL import ImageFont, ImageDraw, Image
import numpy as np
import cv2

# Load the image
image = cv2.imread('./test/images/zidane.jpg')

# Convert the image from OpenCV to PIL
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
pil_image = Image.fromarray(image)

# Set the font and size
font = ImageFont.truetype('Arial.ttf', 32)

# Set the position of the text
position = (10, 50)

# Set the color of the text (RGB)
color = (255, 0, 0)

# Draw the text on the image
draw = ImageDraw.Draw(pil_image)
draw.text(position, 'Xin chào', font=font, fill=color)

# Convert the image back to OpenCV
image = np.array(pil_image)
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# Show the image
cv2.imshow('Image', image)
cv2.waitKey(0)

