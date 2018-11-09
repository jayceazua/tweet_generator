import random
import sys


def get_words():
    """ Opens the file and split it into a list """
    with open('/usr/share/dict/words') as dictionary_file:
        dictionary_words = dictionary_file.read()
    # split('\n') returns the last index of the list with a empty string
    # use splitlines() to now allow that.
    return dictionary_words.splitlines()

def user_input(int):
    """ Make sure that the user is putting in an integer """
    user_input = sys.argv[1]
    if type(user_input) != 'int':
        return 'Invalid Input; please input a integer.'
    else:
        return user_input
