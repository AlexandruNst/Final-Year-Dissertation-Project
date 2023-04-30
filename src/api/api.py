from flask import Flask, request
import time
from main import *
import numpy as np

app = Flask(__name__)
np_array = []


@app.route('/file', methods=['POST'])
def post_model_subject():
    raw_data = request.data.decode('utf-8')
    ply_file = open("./data/user_input/read_ply_file.ply", "w")
    ply_file.write(raw_data)
    time.sleep(2)
    return {"Done writing": ply_file.close()}


@app.route('/register')
def get_register_icp():
    return {"done reg": register_icp()}