# main script, uses other modules to generate sentences
from flask import Flask
from histogram import Dictogram
import cleanup
import tokenize
import word_count
import sample
import sentence



app = Flask(__name__)

@app.route('/')
def home():
    # return for custom code
    return "Hello Jasmine!"

@app.route('/tweeter')
def tweet():
    return "Tweet Generator goes here"

@app.route('/favorite')
"""
... display all the words that have been "favorited" by users.
This is advanced stuff: you'll need to use a database. Not for the faint of heart.
"""
def favorite():
"""
Generate a specific number of words given in a URL query string parameter.
For example, visiting /?num=10 would generate a set of 10 words.
"""
    return "Something is coming up soon..."

# define some functions that compose the above modules

if __name__ == '__main__':
    # code to run when file is executed
    app.run(debug=True, host='0.0.0.0', port=port)
