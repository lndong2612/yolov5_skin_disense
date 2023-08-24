import os
import sys
import cv2                 
import logging
from pathlib import Path
from flask import Flask, request
from detect import detect_object

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

app = Flask(__name__)
app.debug = True
app.logger.setLevel(logging.DEBUG)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/detect_object", methods=['POST'])
def detect_method():
    weights='./public/files/weight_init/best.pt' # model path
    device = '' # cuda device, i.e. 0 or 0,1,2,3 or cpu
    data = './data/coco.yaml'        
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = file.filename
        classified = detect_object(weights, device, data, filename)
    result_dict = {'output': classified}
    return result_dict
  
def run_server_api():
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":     
    run_server_api()