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

import time
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

def draw_bboxes(im, classified, det):
    image_h, image_w, _ = im.shape
    print('{} {}'.format(image_h, image_w))
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y %H:%M:%S", named_tuple)
    # if len(det) == 0:
    #     bbox_mess = 'Không chuẩn đoán được bệnh !!'
    #     fontScale = 0.75
    #     bbox_thick = int(0.6 * (image_h + image_w) / 350)
    #     # Write text on input image
    #     cv2_im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)# Convert the image to RGB (OpenCV uses BGR)
    #     pil_im = Image.fromarray(cv2_im_rgb)# Transform the cv2 image to PIL
    #     draw = ImageDraw.Draw(pil_im)
    #     font = ImageFont.truetype("arial.ttf", 20, encoding="unic")# Use a truetype font
    #     draw.text((5, 10), bbox_mess, font=font, fill=(0, 255, 0))# Draw the text on the image
    #     draw.text((image_w - 190,  image_h - 30), time_string, font=font, fill=(255, 255, 255))# Draw the text on the image
    #     im = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)# Get back the image to OpenCV

    # else:
    fontScale = 0.5
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
        cv2.putText(im, time_string, (image_w - 190,  image_h - 30), cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale, (0, 0, 0), bbox_thick // 2, lineType=cv2.LINE_AA)        
        
    cv2_im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)# Convert the image to RGB (OpenCV uses BGR)
    pil_im = Image.fromarray(cv2_im_rgb)# Transform the cv2 image to PIL
    draw = ImageDraw.Draw(pil_im)
    font_date = ImageFont.truetype("arial.ttf", 15, encoding="unic")# Use a truetype font
    draw.text((image_w - 190,  image_h - 30), time_string, font=font_date, fill=(255, 255, 255))# Draw the text on the image
    im = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)# Get back the image to OpenCV

    return im

def write_date(image, bbox_mess, size, h, w, color, detect_none):
    cv2_im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)# Convert the image to RGB (OpenCV uses BGR)
    pil_im = Image.fromarray(cv2_im_rgb)# Transform the cv2 image to PIL
    font = ImageFont.truetype("arial.ttf", size, encoding="unic")# Use a truetype font
    draw = ImageDraw.Draw(pil_im)
    shape = [(3, 8), (370, 35)]   
    if detect_none == True:
        draw.rectangle(shape, fill = (255, 255, 255))
    draw.text((w, h), bbox_mess, font=font, fill=color)# Draw the text on the image

    image = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)# Get back the image to OpenCV

    return image

image = cv2.imread('./test/images/skin_disense/haclao2.jpg')
bbox_mess = 'Mô hình không chuẩn đoán được bệnh !!'
h = 10
w = 5
color = (0, 0, 0)
size = 15
named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%d/%m/%Y %H:%M:%S", named_tuple)
image_h, image_w, _ = image.shape
im = write_date(image, time_string, size, image_h - 25, image_w - 145, color, detect_none = False)
# im = write_date(image, bbox_mess, size, h, w, color, detect_none = True)


# classified = {'content': [{'label': 'Zona', 'score': '0.92', 'xmax': 599, 'xmin': 87, 'ymax': 362, 'ymin': 44}, {'detected_image': 'resources/images/2023/09/11/detect/08381911092023_detected.jpg', 'original_image': 'resources/images/2023/09/11/original/08381911092023_original.jpg'}], 'status_code': 200}
# det = []
# im_show = draw_bboxes(image, classified, det)
cv2.imshow("IMG", im)
cv2.waitKey(0)
