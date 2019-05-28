#!/usr/bin/env python

from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    print request.form
    return "Hey this is blue, who apparently is in denial and doesn't know how to express her feelings and makes eveyrhting sooooo difficult with her mind. But really its toally fine because I'm not crazy because if you don't think you'll loose your brain"
