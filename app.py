# -*- coding: utf-8 -*-
from flask import Flask
from hashlib import new
from importlib.resources import path
from flask import Flask,render_template,send_from_directory
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello, world'

if __name__ == '__main__':
    app.run()