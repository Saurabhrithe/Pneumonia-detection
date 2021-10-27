from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import cv2 as cv
import numpy as np
import os

app = Flask(__name__)

model = load_model('model.h5')
Dict = {0: 'Normal', 1: "Pneumonia"}


def predict_label(imgPath):
    imgSize = (224, 224)
    img = cv.imread(imgPath)
    img = cv.resize(img, imgSize)
    img = img.astype(np.float32)/255.
    finalImg = np.expand_dims(img, axis=0)
    result = np.argmax(model.predict(finalImg), axis=-1)[0]
    re = Dict[result]
    
    if re == "Pneumonia":
        return "Pneumonia Positive"
    return re


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def get_output():
    if request.method == 'POST':
        img = request.files['my_image']
        img_path = "static/" + img.filename
        img.save(img_path)
        p = predict_label(img_path)
        os.remove(img_path)
        return render_template("index.html", prediction=p)

# main driver function
if __name__ == '__main__':
    app.run()
