from histogram_dictionary import Histogram
import random
# import sys

"""Returns a number of words based on the weight they represent
    within a sample test. Input: Dictionary of words / Output:
    random word based on cummulative weight"""

#strict for python 3.6 to stablish parameters' type
def get_random_word(histogram: dict) -> str:
    # if the lenght of my histogram dictionary
    if len(histogram) == 0:
        return None

    # variable for measuring the probability of a word (float)
    cummu_wght = 0

    #calling a random number from 0 to 1 (float)
    random_num = random.random()

    #iterating through my histogram with the item properties
    for key, value in histogram.items():

        #calculating my percentage of a word based on the value
        type_percentage = value / sum(histogram.values())

        cummu_wght += type_percentage

        #if my random number is less than the weight of a word, don't add it
        if random_num <= cummu_wght:
            return key
            #import pdb; pdb.set_trace() # debugging
