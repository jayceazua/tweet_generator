from flask import Flask
# import the files needed to generate sentences

app = Flask(__name__)

@app.route('/')
def home():
    # return for custom code 
    return "Hello Jasmine!"

@app.route('/tweeter')
def tweet():
    return "Tweet Generator goes here"
