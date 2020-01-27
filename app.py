#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:05:05 2020

@author: hteza
"""

import flask
import pickle
import numpy as np

app=flask.Flask(__name__)

heart=pickle.load(open("logregheart.pkl","rb"))

@app.route("/")
def home():
    return """
            <body>
            <h1>Heart Disease Prediction<h1>
            </body>"""

@app.route("/page")
def page():
    with open("page.html","r") as viz_file:
        return viz_file.read()

@app.route("/predict",methods=["GET"])
def predict():
    thal=flask.request.args["thal"]
    cp=flask.request.args["cp"]
    slope=flask.request.args["slope"]
    exang=flask.request.args["exang"]
    ca=flask.request.args["ca"]
    
    fmap = {"normal":[1,0,0],
            "fixed_defect":[0,1,0],
            "reversible defect":[0,0,1],
            "typical angina":[1,0,0,0],
            "atypical angina":[0,1,0,0],
            "non-anginal pain":[0,0,1,0],
            "asymptomatic":[0,0,0,1],
            "upsloping":[1,0,0],
            "flat":[0,1,0],
            "downsloping":[0,0,1]
            }
    
    X_new = np.array(fmap[thal],fmap[cp],fmap[slope]+[int(exang)]+[int(ca)]).reshape(1,-1)
    y_hat=heart.predict(X_new)
    if y_hat[0]==1:
        outcome = "Heart Disease"
    else:
        outcome = "Normal"
    prob = heart.predict_proba(X_new)
    
    return "This patient is diagnosed as "+outcome+ " with probability "+ str(round(prob[0][1],2))

if __name__== "__main__":
    """Connect to Server"""
    HOST = "127.0.0.1"
    PORT = "4000"
    app.run(HOST,PORT)
    