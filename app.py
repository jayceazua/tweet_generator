# main script, uses other modules to generate sentences
from flask import Flask
import cleanup
import tokenization
import word_count
import sample
import sentence
import sys
from histogram import Dictogram 



app = Flask(__name__)

@app.route('/')
def home():
    file_corpus = "One dog two dog red dog blue dog"
    test = Dictogram(file_corpus)
    return test.random_word()

@app.route('/tweeter')
def tweet():
    return "Tweet Generator goes here"

@app.route('/favorite')
def favorite():
    return "Something is coming up soon..."

# @app.route('/?num={}'.format(input))
# def page_number():
    # return "Something is coming up soon..."

# define some functions that compose the above modules

if __name__ == '__main__':
    # code to run when file is executed
    app.run(debug=True, host='0.0.0.0', port=port)
