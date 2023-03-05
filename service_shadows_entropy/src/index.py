from flask import Flask , request, jsonify
from flask_cors import CORS
from io import BytesIO
import base64
import cv2
import numpy as np

from controller.entroy_many_factor_e_void import entroy_many_factor_e_void
from controller.entroy_many_factor_e_solid import entroy_many_factor_e_solid
from controller.sum_of_solid_and_void import sum_of_solid_and_void
import os

app = Flask(__name__) 
CORS(app)

@app.route('/api/debug', methods = ['GET'])
def debuging():
    if request.method == 'GET':
        return "OK"

@app.route('/api/shadows_entropy', methods = ['POST'])
def calculate_color():
    if request.method == 'POST':
        counting_white = 0
        req = request.get_json(force=True) 
        img_base64 = req['img']
        set_convert = base64.b64decode(img_base64)
        img = BytesIO(set_convert)
        image = cv2.imread(img)
        total_vol_image =  image.shape[0] * image.shape[1]
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)
        thresh = np.array(thresh)
        flatten_thresh = thresh.flatten(order='A')
        
        for i in flatten_thresh: 
            if i == 255:
                counting_white += 1
        
    e_solid = entroy_many_factor_e_solid(counting_white, total_vol_image)
    e_void = entroy_many_factor_e_void(counting_white, total_vol_image) 
    value_entroy = sum_of_solid_and_void(e_solid=e_solid,e_void=e_void)

    return value_entroy


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port=8081)


