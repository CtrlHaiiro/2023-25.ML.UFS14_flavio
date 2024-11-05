import logging
import json
import glob
import sys
from os import environ
from flask import Flask
from keras import models
import numpy as np

logging.debug('Init a Flask app')
app = Flask(__name__)


def doit():
    model = models.load_model("abalone_model.keras")
    predict_input = np.array([
        [0.475,0.37,0.125,0.5095,0.2165,0.1125,0.165,9]
    ])
    predict_result = model.predict(predict_input)

    return json.dumps({"predict_result": predict_result.tolist()})

@app.route('/ping')
def ping():
    logging.debug('Hello from route /ping')

    return doit()
