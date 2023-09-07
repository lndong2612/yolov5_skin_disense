import os
import sys 
WORKING_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(WORKING_DIR, "../"))
import cv2
import json
import time
import logging
import numpy as np
from config import settings
from detect import detect_object
from utils.plots import draw_bboxes
from flask import Flask, request, jsonify, send_file

# [logging config
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(filename)s:%(funcName)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)
# logging config]

app = Flask(__name__)

original = []
detected = []

@app.route("/detect_object", methods=['POST'])
def detect_method():
    try:
        time_tuple = time.localtime()
        time_string = time.strftime('%H%M%S%d%m%Y', time_tuple)
        weight_path = os.path.join(settings.MODEL, 'best.pt') # model path
        original_folder = os.path.join(settings.IMAGE_FOLDER, time.strftime(f"%Y/%m/%d"), 'original') # original image folder path
        detected_folder = os.path.join(settings.IMAGE_FOLDER, time.strftime(f"%Y/%m/%d"), 'detect')# detected image folder path
        if not os.path.exists(original_folder):
            os.makedirs(original_folder)
        if not os.path.exists(detected_folder):
            os.makedirs(detected_folder)

        device = '' # cuda device, i.e. 0 or 0,1,2,3 or cpu
        file = request.files.get('file')
        npimg = np.fromfile(file, np.uint8)
        image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
        input_image = '{}/{}_original.jpg'.format(original_folder, time_string) # original image path
        cv2.imwrite(input_image, image)
        original.append(input_image)
        classified = detect_object(weight_path, device, settings.DATA_COCO, input_image) # objects detection on image
        im_show = draw_bboxes(image, classified) # drawing bboxes on image
        output_image = '{}/{}_detected.jpg'.format(detected_folder, time_string)
        cv2.imwrite(output_image, im_show)
        detected.append(output_image)
        image_url = {
            'original_image': original[-1].replace('\\','/').split('./')[-1],
            'detected_image': detected[-1].replace('\\','/').split('./')[-1]
        }

        classified.append(image_url)

        with open(os.path.join(settings.IMAGE_FOLDER, 'image_url.json'), 'w') as outfile:
            json.dump(image_url, outfile)

        return jsonify(status_code = 200, content=classified)

    except Exception as e:
        return jsonify(status_code = 400, content={'success':"false",'error': str(e)})

@app.route('/download', methods=['GET', 'POST'])
def download():
    try:
        """Download a file."""
        with open(os.path.join(settings.IMAGE_FOLDER, 'image_url.json'), "r") as outfile:
            json_object = json.load(outfile)
            path = os.path.join(os.getcwd(),"{}".format(json_object['detected_image']))
        return send_file(path, as_attachment=True)

    except Exception as e:
        return jsonify(status_code = 400, content={'success':"false",'error': str(e)})

def run_server_api():
    host = settings.HOST
    port = int(settings.PORT)
    app.run(host=host, port=port, debug=settings.DEBUG)

if __name__ == "__main__":
    run_server_api()