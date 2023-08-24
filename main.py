import os
import sys
import cv2                 
import logging
import numpy as np
from pathlib import Path
from flask import Flask, request, jsonify
from detect import detect_object

app = Flask(__name__)
app.debug = True
app.logger.setLevel(logging.DEBUG)


@app.route("/detect_object", methods=['POST'])
def detect_method():
    try:
        weights='./public/files/weight_init/best.pt' # model path
        device = '' # cuda device, i.e. 0 or 0,1,2,3 or cpu
        data = './data/coco.yaml'        
        file = request.files.get('file')
        npimg = np.fromfile(file, np.uint8)
        image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
        filename = 'photo.jpg'
        cv2.imwrite(filename, image)
        classified = detect_object(weights, device, data, filename)
        return jsonify(status_code=200, content=classified)
    
    except Exception as e:
        return jsonify(status_code=400, content={'success':"false",'error': str(e)})

def run_server_api():
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":     
    run_server_api()