import logging
import json
import glob
import sys
from os import environ
from flask import Flask
import joblib
import sklearn
import numpy as np
from flask import request


logging.debug('Init a Flask app')
app = Flask(__name__)


def doit(lunghezza, diametro):
    
    model_dir = environ['SM_MODEL_DIR']
    print(f"######## La model dir è: {model_dir}")
    model = joblib.load(f"{model_dir}/output.joblib")
    
    predict_input = np.array([
        [Square_Footage,Num_Bedrooms,Num_Bathrooms,Year_Built,Lot_Size,Garage_Size,Neighborhood_Quality,3058,2,1,2017,1.498552073529678,0,2]
    ])
    predict_result = model.predict(predict_input)

    return json.dumps({
        "inputs": predict_input.tolist(),
        "predict_result": predict_result.tolist()
    })

@app.route('/ping')
def ping():
    print(f"######## /PINGGGGGG")

    return 'Hello, World!'

# see https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html#your-algorithms-inference-code-container-response
@app.route('/invocations', methods=['POST'])
def invocations():
    print(f"######## /INVOCATIONSSSS")
    http_request_post_payload = request.json
    print("######### http_request_post_payload: {}".format(http_request_post_payload))

    SqF = request.args.get('Square_Footage')
    NBe = request.args.get('Num_Bedrooms')
    NBa = request.args.get('Num_Bathroom')
    YeB = request.args.get('Year_Built')
    LoTS = request.args.get('Lot_Size')
    GS = request.args.get('Garage_Size')
    NeQ = request.args.get('Neighborhood_Quality')
    return doit(SqF, NBe, NBa, YeB, LoTS, GS, NeQ)