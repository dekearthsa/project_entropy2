from flask import Flask , request
from flask_cors import CORS
import numpy as np
import cv2
import base64
 

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
        try:
            req = request.get_json(force=True)
            # print(req['data'])
            image_data = base64.b64decode(req['data'])
            np_array = np.frombuffer(image_data, np.uint8)
            img = cv2.imdecode(np_array, cv2.IMREAD_UNCHANGED)
            # decoded_data = base64.b64decode(req['data'])
            # np_data = np.fromstring(decoded_data,np.uint8)
            # filestr = request.files['file'].read()
            # file_bytes = np.fromstring(filestr, np.uint8)
            # img = cv2.imdecode(np_data, cv2.IMREAD_UNCHANGED)
            entropy_out = shannon_entropy(img[:,:,0])
            # print(entropy_out)
            if entropy_out != 0:
                return str(round(entropy_out,3))
            else:
                return 0

            # try:    
            #     entropy_out = shannon_entropy(img[:,:,0])
            #     print(entropy_out)
            #     return "color entropy => " + str(entropy_out)
            # except:
            #     entropy_out = shannon_entropy(img[:,:,0])
            #     print(entropy_out)
            #     return "color entropy => " + str(entropy_out)

            # if entropy_out <= 0.0:
            #     print("none")
            # else:
            #     return 
            
            # return "OK"
        

            # print(request.files)
            # filestr = request.files['file'].read()
            # file_bytes = np.fromstring(filestr, np.uint8)
            # img = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)
            # entropy_out = shannon_entropy(img[:,:,0])
            # return "color entropy => " + str(entropy_out)
        except:
            return 0

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8085)

