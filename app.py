# main script, uses other modules to generate sentences
from flask import Flask
import cleanup
import tokenization
import word_count
import sample
import sentence
import sys
from histogram import Dictogram
from markov_chain_first import get_long_words, first_order_markov, tweet_generator



app = Flask(__name__)

@app.route('/')
def home():
    clean_data = get_long_words()
    markov_chn_dict = first_order_markov(clean_data)

    return tweet_generator(30, markov_chn_dict)

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
