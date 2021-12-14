import tflite_runtime.interpreter as tflite
from PIL import Image
import numpy as np
import io
import requests


interpreter = tflite.Interpreter(model_path='best_model.tflite')
interpreter.allocate_tensors()
input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']


#url = 'https://raw.githubusercontent.com/CemKeskin84/ML-Zoomcamp/main/capstone_project/sample_images/sample_with_mask.png'


def predict(url):
    r = requests.get(url)
    img = Image.open(io.BytesIO(r.content))
    img = img.resize((100, 100), Image.NEAREST)
    x = np.array(img, dtype='float32')
    X = np.array([x])
    X /= 255

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    pred = interpreter.get_tensor(output_index)

    float_predictions = pred[0].tolist()

    result = {'Mask(0=with & 1=without)': round(float_predictions[0],2)}

    return result


def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result