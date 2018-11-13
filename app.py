from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Jasmine!"

@app.route('/tweeter')
def tweet():
    return "Tweet Generator goes here"
