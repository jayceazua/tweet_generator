# def get_words():
#     """ Opens the file and split it into a list """
#     with open('sherlock_corpus.txt') as dictionary_file:
#         dictionary_words = dictionary_file.read()
#     # split('\n') returns the last index of the list with a empty string
#     # use splitlines() to now allow that.
#     return dictionary_words.split(' ')

def get_words(source_text):
    words = source_text.lower().split()
    return words

# As a list of lists:
def list_histogram(source_text):
    histogram = []
    # loop through the source text list
    for word in source_text: # O(n)
    	found_duplicate = False
    	for item in histogram: # O(n^2)
    		if word == item[0]:
    			item[1] += 1
    			found_duplicate = True
    			break
    	if not found_duplicate:
    		histogram.append([word, 1])
    return histogram

# As a list of tuples:
def tup_histogram(source_text):
	temp_histo = [] # this is a temp list for the cause of it being mututable
	for word in source_text: # O(n) - could be better
		found_duplicate = False
		for item in temp_histo: # O(n^2) - could be better
			if word == item[0]:
				item[1] += 1
				found_duplicate = True
				break
		if not found_duplicate:
				temp_histo.append([word, 1])
	histogram = [tuple(i) for i in temp_histo]
	return histogram

# As a dictionary of key-value pairs:
def dic_histogram(source_text):
    """ return a histogram data structure that stores each unique word
    along with the number of times the word appears in the source text. """
    words = source_text
    histogram = {}
    for word in words:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram

# As a count histogram:
def count_histogram(source_text):
    pass

def unique_words(histogram):
    """ returns the total count of unique words in the histogram """
    counter = 0 # I decided to go with this instead of just using a set or len function to get practice.
    for word in histogram:
        counter += 1
    return counter

def frequency(word, histogram):
    """ returns the number of times that word appears in a text. """
    if word in histogram:
        return histogram[word]
    else:
        return "Error: Word is not in corpus."


# run the code
if __name__ == "__main__":
    source_text = "one fish two fish red fish blue fish"
    file = get_words(source_text)
    histogram = dic_histogram(file)
    print(histogram)
    word = "fish"
    print(frequency(word, histogram))


"""
#######################################################
# Histogram - Analyze Word Frequency in Text
import sys
import random

file_corpus = "One fish two fish red fish blue fish"
# open_file = open(file_corpus)
# read_file = open_file.read()

########## ########## ########## ##########
# list of counts
def list_of_counts(source_text):
	list_source_text = source_text.split()
	# results have to look like:
	# counts_list = [(1, ['one', 'two', 'red', 'blue']), (4, ['fish'])]

# list of tuples
def list_of_tuples(source_text):


########## ########## ########## ##########
# Step 1. Listogram
def list_of_lists(source_text):


# Step 2. Listogram
def frequency_list(word, histogram):
	# lower case the word input
	word_use = word.lower()
    # loop through the list of lists
	for item in histogram:
		# check if the word input is in the dictionary
		if word_use in item[0]:
			# if so return the value
			return item[1]

########## ########## ########## ##########
# 1. What is the least/most frequent word(s)?
# 2. How many different words are used?
def uniqie_words (histogram):
	return len(histogram)
# 3. What is the average (mean/median/mode) frequency of words in the text?

def source_text(corpus):
	"
        This function gets a corpus and splits it into a list.
	"
	return corpus.lower().split()

def source_text_len():
	"
	    This function gets the length of the corpus after splitting into a list.
	"
	return len(source_text())



########## ########## ########## ##########


########## ########## ########## ##########
# Testing
def test_relative():
	histogram = dict_histogram(corpus)
	temp_results = []
	for i in range(0, 10000):
		temp_results.append(random_word(corpus, histogram))
	for word in histogram:
		print 'This is the results for ' + word + ':'
		print temp_results.count(word)

########## ########## ########## ##########

class Dictogram(object):

	def __init__(self, corpus=None):
		self.corpus = corpus
		self.corpus_list = self.corpus.lower().split()
		self.histogram = self._dict_histogram()
		self.tokens = len(self.corpus_list)

	def _dict_histogram(self):
		"
	        This creates a Dictogram with a source text.
		"
		histogram = {}
		for word in self.corpus_list:
			if word in histogram:
				histogram[word] += 1
			else:
				histogram[word] = 1
		return histogram

	def frequency(self, word):
    	# lower case the word input
		word_use = word.lower()
    	# check if the word input is in the dictionary
		if word_use in self.histogram:
        	# if so return the value
			return self.histogram[word_use]

	def probabilities_frequency(self, word):
	    # call the frequency_word function and
		# allow of the int to be a float
		frequency = float(self.frequency(word))
	    # return the result
		return frequency / self.tokens

	# Step 4. Dictogram
	def random_word(self):
		"
		Stochastic Sampling for dictionaries.
		"
	    # generate a random float integer from 0 to 1
		random_num = random.uniform(0, 1)
	    # this variable is used to update as we loop
		running_total = 0.0
	    # loop through the dictionary histogram
		for key, value in self.histogram.items():
	        # runs the probabilities_frequency function and adds it to the running_total variable
			running_total += self.probabilities_frequency(key)
	        # if the running_total variable is equal to our greater than the random_num
			if running_total >= random_num:
	            # return the current key of the loop it is in and break out of it
				return key



if __name__ == "__main__":
	x = "One dog two dog red dog blue dog"
	test = Dictogram(file_corpus)
	print(test.histogram)
	print(test.tokens)
	print(test.random_word())

# listogram:
class Listogram(list):
    "Listogram is a histogram implemented as a subclass of the list type."

    def __init__(self, word_list=None):
        "Initialize this histogram as a new list and count given words."
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        "Increase frequency count of given word by given count amount."
        # TODO: Increase word frequency by count

    def frequency(self, word):
        "Return frequency count of given word, or 0 if word is not found.
        # TODO: Retrieve word frequency count

    def __contains__(self, word):
        "Return boolean indicating if given word is in this histogram."
        # TODO: Check if word is in this histogram

    def _index(self, target):
        "Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."
        # TODO: Implement linear search to find index of entry with target word


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())
    """
