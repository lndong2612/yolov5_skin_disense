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

import os
import time
import json
from config import settings

# time_tuple = time.localtime()
# time_string = time.strftime('%H%M%S%d%m%Y', time_tuple)

# folder = "./nhap" # model path
# input_img = 'original'
# output_img = 'detect'
# input_image_path = time.strftime(f"{folder}/{input_img}/%Y/%m/%d/")
# output_image_path = time.strftime(f"{folder}/{output_img}/%Y/%m/%d")
# if not os.path.exists(input_image_path):
#     os.makedirs((input_image_path), exist_ok=True)
# if not os.path.exists(output_image_path):
#     os.makedirs((output_image_path), exist_ok=True)

image_url = {
    'original': 'sfsafadfdf',
    'detect': 'rweykkhmtjh'
}
with open("sample.json", "r") as outfile:
    # json.dump(image_url, outfile)
    json_object = json.load(outfile)
    print(json_object['original'])
