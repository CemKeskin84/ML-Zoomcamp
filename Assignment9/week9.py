import tflite_runtime.interpreter as tflite
import numpy as np
from io import BytesIO
from urllib import request
from PIL import Image


def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img

def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def preprocess_input(x):
    rescaled = x / 255
    return rescaled.astype(np.float32)


def predict(url):
    target_size = (150,150)
    img = download_image(url)
    img = prepare_image(img, target_size=target_size)
    x = np.array(img)
    X = np.array([x])
    X = preprocess_input(X)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    pred = interpreter.get_tensor(output_index)

    return pred


interpreter = tflite.Interpreter(model_path='dogs-cats-model.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']


url = 'https://upload.wikimedia.org/wikipedia/commons/9/9a/Pug_600.jpg'

pred = predict(url)

print(pred)