import os
import sys 
WORKING_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(WORKING_DIR, "../"))
import cv2       
import numpy as np
from flask import Flask, request, jsonify
from detect import detect_object
from config import settings
from utils.plots import draw_bbox

app = Flask(__name__)


@app.route("/detect_object", methods=['POST'])
def detect_method():
    try:
        weight_path = "./resources/weight_init/best.pt" # model path
        image_path = "./resources/images" # model path
        device = '' # cuda device, i.e. 0 or 0,1,2,3 or cpu
        data = './data/coco.yaml'
        file = request.files.get('file')
        npimg = np.fromfile(file, np.uint8)
        image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
        inputname = 'photo.jpg'
        cv2.imwrite(image_path + '/' + inputname, image)
        classified = detect_object(weight_path, device, data, image_path + '/' + inputname)
        im_show = draw_bbox(image, classified)
        outputname = 'detect.jpg'
        cv2.imwrite(image_path + '/' + outputname, im_show)
        return jsonify(status_code=200, content=classified)

    except Exception as e:
        return jsonify(status_code=400, content={'success':"false",'error': str(e)})

def run_server_api():
    host = settings.HOST
    port = int(settings.PORT)
    app.run(host=host, port=port, debug=settings.DEBUG)

if __name__ == "__main__":
    run_server_api()