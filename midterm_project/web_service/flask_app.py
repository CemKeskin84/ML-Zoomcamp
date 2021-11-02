# THis file contains the code for energy prediction service
# that is currently running on cemk.pythonanywhere.com
# Having a beginner account in pythonanywhere.com, uploading this
# and the model.bin file is sufficient to standby the web-service.
# The code for the client is provided in another file in the same 
# folder (/web_service).


from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

print("dd")

with open('mysite/model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)


@app.route('/predict', methods=['POST'])
def predict():
    building = request.get_json()

    X = dv.transform([building])
    y_pred = model.predict(X)

    result = {
        'heating': round(float(np.exp(y_pred[0,0])), 2),
        'cooling': round(float(np.exp(y_pred[0,1])), 2)
        }
    return jsonify(result)