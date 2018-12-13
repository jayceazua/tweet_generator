import re
import string

def get_long_words():
    dictionary_long_words = ''
    with open('test_corpus.txt') as dictionary_long_file:
        dictionary_long_words += dictionary_long_file.read().lower().replace('\n', ' ')
        result_long = []
        #this function cleans my punctuation
        clean = remove_punctuation(dictionary_long_words)
        #this method returns each of my words in a list
        no_regex = re.findall("[A-z]+\'?[A-z]*|\$[0-9]*", clean)
    #this loop puts all my words together
    for found_long_reg_exp in no_regex:
        result_long.append(found_long_reg_exp)
    #returns a string of words with no punctuation
    return str(result_long)

def get_short_words():
    corpus = 'one fish two fish three fish four fish red fish blue fish'
    return corpus

# This function is replacing all of my special chars with spaces
def remove_punctuation(sample_text):
    remove_text = re.sub('[,.()]', '', sample_text)
    remove2_text = re.sub('--', ' ', remove_text)
    remove3_text = re.sub(':', ' ', remove2_text)
    remove4_text = re.sub('/(?<!\S).(?!\S)\s*/', '', remove3_text)
    #text cleaned with no words
    return remove4_text
