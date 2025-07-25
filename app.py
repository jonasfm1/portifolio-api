import os
from flask import Flask, jsonify, json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS-HEADERS'] = 'Content-Type'
@app.route('/')
@cross_origin()
def index():
    personal_info = os.path.join('pages/home/personal_info.json')
    with open(personal_info) as info:
        data = json.load(info)
        return data

@app.route('/companies')
@cross_origin()
def company():
    personal_info = os.path.join('pages/companies/companies_names.json')
    with open(personal_info) as info:
        data = json.load(info)
        return data

@app.route('/education')
@cross_origin()
def education():
    personal_info = os.path.join('pages/education/education.json')
    with open(personal_info) as info:
        data = json.load(info)
        return data

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
