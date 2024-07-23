from flask import Flask
import requests


app = Flask(__name__)

@app.route('/')
def hello_world():
    return {'hello': 'world'}


@app.route('/first')
def first():
    return {'single': 'route'}


@app.route('/second')
def second():
    data = {
        "key": "value",
    }
    response = requests.post('http://second-microservice-service/single', json=data)
    return response.json()
