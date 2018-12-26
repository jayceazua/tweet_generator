# module for turning clean source text into a list of tokens
import random
import re
import sys
import cleanup

def token_list(corpus):
    token_list = re.split(' ', corpus)
    token_list.pop()
    return token_list
