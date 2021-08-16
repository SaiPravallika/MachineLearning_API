import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import json

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict_api/',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    output = ""
    
    try:
        
        data = request.get_json(force=True)
        data_received = [ data['Time'],data['V1'],data['V2'],data['V3'],data['V4'],data['V5'],data['V6'],data['V7'],data['V8'],
                        data['V9'],data['V10'],data['V11'],data['V12'],data['V13'],data['V14'],data['V15'],
                      data['V16'],data['V17'],data['V18'],data['V19'],data['V20'],data['V21'],data['V22'],data['V23'],data['V24'],
                        data['V25'],data['V26'],data['V27'],data['V28'],data['Amount']]

        X_test = np.array(data_received)

        X_test = X_test.reshape(1,30)

        #print(X_test)

        prediction = model.predict(X_test)

        output = str(prediction[0])

        #print(output)

        s= json.dumps(output)
        #print(s)


        return render_template('index.html', prediction_text=json.dumps(output))
    
    except(ValueError, KeyError, TypeError):
           
            return 'Error occured due to missing values/key error/type error! Please input the features in required format!'
        
    

if __name__ == "__main__":
    app.run(debug=True)