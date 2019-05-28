#!/usr/bin/env python

from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    print request.form
    return "This will print on the server, the form parameters"
