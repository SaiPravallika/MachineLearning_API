import requests
import json

url = 'http://localhost:5000/predict_api/'
#data = []

data = json.dumps({"Time": 45014.000000, "V1":-2.004881, "V2":-1.127553, "V3":0.563607,"V4": 0.143416,"V5": 1.358909,"V6": -0.983896,"V7": -0.755049,"V8":  0.658284,"V9": -0.624140,"V10": -0.538880,"V11": 0.797106,"V12": 0.736617,"V13": -0.365795,"V14": 0.828498,"V15": -0.058298,"V16": -0.568928,"V17": 0.471337,"V18": -0.205489,"V19": 1.223548,"V20": 0.471835,"V21": 0.286698,"V22": 0.149270,"V23": -0.209613,"V24": -0.187195,"V25": -0.250038,"V26": 1.172414,"V27": -0.044708,"V28": -0.272800,"Amount": 2.370000})

#headers = {'content-type': 'application/json'}
#headers = {'Content-Type':'application/json'}
headers = {
    'Content-Type': 'application/json;charset=UTF-8'
}

r = requests.post(url, data)

#print(r.text)

#print(r.json())


