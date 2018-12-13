# main script, uses other modules to generate sentences
from flask import Flask
import word_frequency
import cleanup
import markov



app = Flask(__name__)

@app.route('/')
def home():
    # Get cleaned data
    file_name = 'test_corpus.txt'
    cleaned_file = cleanup.clean_file(file_name)
    # Create data structure
    data_structure = markov.make_higher_order_markov_model(3, cleaned_file)
    # Pass data structure to get random setence with 140 chars
    random_sentence = markov.generate_random_sentence_n(140, data_structure)

    return random_sentence

@app.route('/tweeter')
def tweet():
    return "Tweet Generator goes here"

@app.route('/favorite')
def favorite():
    return "Something is coming up soon..."


if __name__ == '__main__':
    # code to run when file is executed
    app.run(debug=True, host='0.0.0.0', port=port)


# from flask import Flask, render_template, request, redirect
# import os
#
# import twitter


# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 5000))
