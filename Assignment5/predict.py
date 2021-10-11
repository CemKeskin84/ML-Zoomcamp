
import pickle
from flask import Flask
from flask import request
from flask import jsonify



with open ('dv.bin', 'rb') as f_in1:
    dv  = pickle.load(f_in1)

with open('model1.bin', 'rb') as f_in2:
    model = pickle.load(f_in2)

app = Flask('Churn')


@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
        
    X = dv.transform([customer])
    y_pred = round(model.predict_proba(X)[0,1],3)
    
    result = {

        'churn_probability': y_pred
    }
    
    return(result)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)






