from flask import Flask


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return {
        "message" : "hello from second ms-service"
    }