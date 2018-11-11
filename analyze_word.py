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
    return len(histogram)

def frequency_dict(word, histogram):
    """ returns the number of times that word appears in a text. """
    if word in histogram: # O(n)
        return histogram[word]
    else:
        return "Error: Word is not in corpus."

def frequency_list_tuple(word, histogram):
    for item in histogram: # O(n)
        if item[0] == word:
            return item[1]


# run the code
if __name__ == "__main__":
    source_text = "one fish two fish red fish blue fish"
    file = get_words(source_text)
    histogram = dic_histogram(file)
    word = "fish"
    print(unique_words(histogram))
    print(frequency_dict(word, histogram))


"""
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
    
"""
