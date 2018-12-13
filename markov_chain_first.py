import random
import re
import string
from stochastic_sampling import get_random_word
from markov_words_helper import get_long_words, get_short_words

#accessing the list of words as string
helper_dictionary_words = get_long_words()
# helper_dictionary_words = get_short_words()

def first_order_markov(str_words):
    tokens = str_words.split(" ")

    markov_dict = {}
    # any order markov chain, just change the variable to the desired number
    # order = 5
    for index, token_key in enumerate(tokens):
        if index == len(tokens) - 1: break
        # next_token = ' '.join(tokens[index + 1: index + 1 + order])
        if token_key not in markov_dict:
            markov_dict[token_key] = {tokens[index + 1]: 1}
            # any order
            # markov_dict[token_key] = {next_token: 1}
        else:
            next_token = tokens[index + 1]
            if next_token not in markov_dict[token_key]:
                markov_dict[token_key][next_token] = 1
            else:
                markov_dict[token_key][next_token] += 1

    return markov_dict

def tweet_generator(order, markov_dict):

    final_sentence = ''

    counter = 0
    #convert a dict to a list
    list_of_words = list(markov_dict)

    #returns to me a random word from the previous list
    first_word = random.choice(list_of_words)

    #loop to attach my random words to sentence
    while counter != order:

        #call my random_word function from my stochastic sampling
        #and index that to my random word
        random_word_sentence = get_random_word(markov_dict[first_word])

        first_word = random_word_sentence

        #append to my sentence string
        final_sentence += random_word_sentence

        sentence = ''.join(final_sentence)

        counter += 1

    remove_more = re.sub(",", '', sentence)
    remove_even_more = re.sub("'", ' ', remove_more)
    # print(remove_even_more)
    # print("test: " + sentence[0])

    return remove_even_more.strip()
    # return final_sentence


if __name__ == "__main__":

    clean_data = get_long_words()

    markov_chn_dict = first_order_markov(clean_data)

    print(tweet_generator(30, markov_chn_dict))
