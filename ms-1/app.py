from flask import Flask
import requests


app = Flask(__name__)

@app.route('/')
def hello_world():
    # make a get request
    requests.get('http://ms2-service')

    # make a post request
    payload = {
        "hello" : "world"
    }
    response = requests.post('http://ms2-service', json=payload)

    return {
        'hello': 'world',
        'response': response.status_code
    }