# Script that randomly rearranges a set of words provided as command-line arguments
import sys
import random

def rearrange(words_list):
    # create and empty list to store randomly generated words from words_list
    rearranged_list = []
    while len(words_list) != 0:
        # generate a random index to work with
        random_index = random.randint(0, len(words_list) - 1)
        # append that random index into the above rearranged_list
        rearranged_list.append(words_list[random_index])
        # remove that word from the words_list to prevent same selection
        words_list.pop(random_index)
    # return a sentence from the randomly selected "sorted" words_list
    return ' '.join(rearranged_list)

def reversal(str):
    # easier way to reverse
    return str[::-1]

if __name__ == "__main__":
    words_list = sys.argv[1:]
    print(rearrange(words_list))
