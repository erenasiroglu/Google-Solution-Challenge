import io
import os

from flask import Flask, request, render_template
from google.cloud import vision
from google.cloud.vision_v1 import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'sigma-current-382014-e51b038d9e80.json'

client = vision.ImageAnnotatorClient()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():
    if request.method == 'POST':
     
        image = request.files['image'].read()
        image = types.Image(content=image)

        response = client.label_detection(image=image)
        labels = response.label_annotations

        return render_template('outcome.html', labels=labels)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()

