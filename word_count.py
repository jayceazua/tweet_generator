# module for generating histograms from a list of tokens
import sys
import cleanup
import tokenization

def dictogram(token_list):
    histogram = {}
    for word in token_list:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1
    return histogram
