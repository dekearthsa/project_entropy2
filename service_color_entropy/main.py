from flask import Flask , request
from flask_cors import CORS
import numpy as np
import cv2
from skimage.measure.entropy import shannon_entropy

app = Flask(__name__) 
CORS(app)

@app.route('/api/debug', methods = ['GET'])
def debuging():
    if request.method == 'GET':
        return "OK"

@app.route('/api/color_entropy', methods = ['POST'])
def calculate_color():
    if request.method == 'POST':
        filestr = request.files['file'].read()
        file_bytes = np.fromstring(filestr, np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)
        entropy_out = shannon_entropy(img[:,:,0])
        return "color entropy => " + str(entropy_out)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8085)

