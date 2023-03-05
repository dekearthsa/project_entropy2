from flask import Flask , request, jsonify
from flask_cors import CORS
from io import BytesIO
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
        req = request.get_json(force=True) 
        img_base64 = req['img']
        set_convert = base64.b64decode(img_base64)
        img = BytesIO(set_convert)

        entropy_out = shannon_entropy(img[:,:,0])
        return entropy_out

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port=8080)


