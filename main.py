from flask import Flask, jsonify, json
import os

app = Flask(__name__)


@app.route('/')
def index():
    personal_info = os.path.join('pages/home/personal_info.json')
    with open(personal_info) as info:
        data = json.load(info)
        return data


@app.route('/companys')
def company():
    personal_info = os.path.join('pages/companys/companys_names.json')
    with open(personal_info) as info:
        data = json.load(info)
        return data


@app.route('/education')
def company():
    personal_info = os.path.join('pages/education/education.json')
    with open(personal_info) as info:
        data = json.load(info)
        return data

app.run(debug=True)
