from flask import Flask , request, jsonify
from flask_cors import CORS
from io import BytesIO
import base64
import os
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
        file = request.files['file']
        file.save(file.filename)
        set_path = "./"+file.filename
        img = cv2.imread(set_path)
        entropy_out = shannon_entropy(img[:,:,0])
        os.remove("./"+file.filename)
        return str(entropy_out)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port=8085)


