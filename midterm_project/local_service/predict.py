import pickle
import numpy as np
from flask import Flask, request, jsonify

model_file = 'model.bin'


with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('energy')

@app.route('/predict', methods=['POST'])
def predict():
    building = request.get_json()
    #print(building)

    X = dv.transform([building])
    y_pred = model.predict(X)
    
    result = {
        'heating': round(float(np.exp(y_pred[0,0])), 2), 
        'cooling': round(float(np.exp(y_pred[0,1])), 2) 
        }
    
    
    #print('result is: ', result )
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)


