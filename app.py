# main script, uses other modules to generate sentences
from flask import Flask
import cleanup
import tokenization
import word_count
import sample
import sentence
import sys
import histogram



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
"""
... display all the words that have been "favorited" by users.
This is advanced stuff: you'll need to use a database. Not for the faint of heart.
"""
def favorite():
    return "Something is coming up soon..."

@app.route('/?num={}'.format(input))
def page_number():
"""
Generate a specific number of words given in a URL query string parameter.
For example, visiting /?num=10 would generate a set of 10 words.
def user_input(): <- use this similar function for the number input into the route
    " Make sure that the user is putting in an integer
    user_input = sys.argv[1]
    if type(user_input) != 'int':
        return 'Invalid Input; please input a integer.'
    else:
        return user_input
"""
    return "Something is coming up soon..."

# define some functions that compose the above modules

if __name__ == '__main__':
    # code to run when file is executed
    app.run(debug=True, host='0.0.0.0', port=port)
