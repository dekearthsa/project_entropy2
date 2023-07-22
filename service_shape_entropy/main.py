from flask import Flask , request, jsonify
from flask_cors import CORS
import cv2
import numpy as np

from src.controller.counting_shape import counting_shape
from src.controller.calculate_shapes_entropy import calculate_shapes_entropy

app = Flask(__name__) 
CORS(app)

@app.route('/api/debug', methods = ['GET'])
def debuging():
    if request.method == 'GET':
        return "OK"

@app.route('/api/shape_entropy', methods = ['POST'])
def calculate_color():
    if request.method == 'POST':
        filestr = request.files['img'].read()
        file_bytes = np.fromstring(filestr, np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)
        
        imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret , thresh = cv2.threshold(imgGry, 150 , 255, cv2.CHAIN_APPROX_NONE)
        contours , hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        shapes_array = []
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
            cv2.drawContours(img, [approx], 0, (0, 0, 255), 5)
            x = approx.ravel()[0]
            y = approx.ravel()[1] - 5
            x, y , w, h = cv2.boundingRect(approx)
            if w >=10 and h >= 10:
                if len(approx) == 3:
                    warping = {
                            "shape_type": str(len(approx))+"-"+"square",
                            "width": w,
                            "height": h,
                            "x":x,
                            "y":y,
                            "value": (1/2)*(w*h)
                        }
                    # cv2.putText( img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0) )
                elif len(approx) == 4 :
                    aspectRatio = float(w)/h
                    # print(aspectRatio)
                    if aspectRatio >= 0.95 and aspectRatio < 1.05:
                        warping = {
                            "shape_type": str(len(approx))+"-"+"square",
                            "width": w,
                            "height": h,
                            "x":x,
                            "y":y,
                            "value": w*h
                        }
                        shapes_array.append(warping)
                        # print("\n")
                        # cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

                    else:
                        warping = {
                            "shape_type": str(len(approx))+"-"+"square",
                            "width": w,
                            "height": h,
                            "x":x,
                            "y":y,
                            "value": w*h
                        }
                        shapes_array.append(warping)
                        # print("\n")
                        # cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

                elif len(approx) == 5 :
                    warping = {
                            "shape_type":  str(len(approx))+"-"+"square",
                            "width": w,
                            "height": h,
                            "x":x,
                            "y":y,
                            "value": w*h
                        }
                    shapes_array.append(warping)
                    # print("\n")
                    # cv2.putText(img, "pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
                elif len(approx) == 6:
                    warping = {
                            "shape_type":  str(len(approx))+"-"+"square",
                            "width": w,
                            "height": h,
                            "x":x,
                            "y":y,
                            "value": w*h
                        }
                    shapes_array.append(warping)
                    # cv2.putText(img, "6-square", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
                else:
                    warping = {
                            "shape_type": "8-"+"square",
                            "width": w,
                            "height": h,
                            "x":x,
                            "y":y,
                            "value": w*h
                        }
                    shapes_array.append(warping)
    export_shape_array = counting_shape(shapes_array)
    cal_entropy = calculate_shapes_entropy(export_shape_array)
    return "shape entropy => " + str(cal_entropy)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port=8082)


