#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:38:00 2020

@author: hteza
"""

import flask
app =  flask.Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

# @app.route("/greet/<name>")
# def greet(name):
#     return "Hello, {} !!!".format(name)

@app.route("/")
def hello():
    return '''
    <header>
    <h1> Flask<sup><font size="2" color="gray">test</font><sup><h1>
    <header>
    <body>
    <font size="8"> Hello World !!! </font>
    <body>
    <footer>
    <font size="4" color="gray"> 
    <sub> basically just hello <sub>
    </font>
    <footer>
    '''

if __name__=="__main__":
    app.run()
    # app.run(debug=True) if you want to debug your web app everytime
    
# app runs on top of localhost:5000 ( http://127.0.0.1:5000/ )
    
    