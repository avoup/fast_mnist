from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse

import numpy as np
import tensorflow as tf
import io
import matplotlib.image as mpimg


app = FastAPI()


def array_from_bytes(file: bytes, extension):
    image = io.BytesIO(file)
    with image:
        image = mpimg.imread(image, format=extension)
    return image


def process_image(image):
    image = image[:, :, :3]
    tsimage = image
    # tsimage = tsimage/255
    tsimage = 255 - tsimage
    tsimage = tf.image.rgb_to_grayscale(tsimage, name=None)
    tsimage = tf.image.resize(tsimage, (28, 28))
    tsimage = tf.squeeze(tsimage)
    tsimage = (np.expand_dims(tsimage, 0))
    return tsimage


def predict(image, model):
    probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
    return np.argmax(probability_model.predict(image)[0])


@app.post("/predict/")
async def prediction(file: UploadFile = File(...)):
    # Load model
    model = tf.keras.models.load_model('/models/mnist_model')

    # Get uploaded file extension
    extension = file.content_type.split('/')[1]

    # Get file as an array from bytes
    image = array_from_bytes(file.file.read(), extension)

    # Resize and Reshape image to (28, 28)
    image = process_image(image)

    # Run prediction
    pred = predict(image, model)
    return {"prediction": int(pred)}


@app.get("/", response_class=FileResponse)
async def main():
    return FileResponse('/code/app/index.html')
