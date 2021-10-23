from flask import Flask, render_template, request
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import os

app = Flask(__name__)

model = load_model('modelXYZ.h5')
model.make_predict_function()
Dict = {0: 'Normal', 1: " Pneumonia"}


def predict_label(img_path):
    i = cv2.imread(img_path)
    sample_image = cv2.resize(i, (224, 224))
    if sample_image.shape[2] == 1:
        sample_image = np.dstack([sample_image, sample_image, sample_image])
    sample_image = cv2.cvtColor(sample_image, cv2.COLOR_BGR2RGB)
    sample_image = sample_image.astype(np.float32) / 255.
    sample_image_processed = np.expand_dims(sample_image, axis=0)
    predictedLabel = np.argmax(model.predict(sample_image_processed), axis=-1)[0]

    return Dict[predictedLabel]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/submit', methods=['GET', 'POST'])
def get_output():
    if request.method == 'POST':
        img = request.files['my_image']
        img_path = "static/" + img.filename
        img.save(img_path)
        p = predict_label(img_path)
        os.remove(img_path)
        return render_template("index.html", prediction=p)


if __name__ == "__main__":
    app.run(debug=True)
