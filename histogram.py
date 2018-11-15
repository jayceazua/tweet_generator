import random

########## ########## ########## ##########
# Testing
def test_relative():
	histogram = dict_histogram(corpus)
	temp_results = []
	for i in range(0, 10000):
		temp_results.append(random_word(corpus, histogram))
	for word in histogram:
		print('This is the results for ' + word + ':')
		print(temp_results.count(word))

########## ########## ########## ##########

class Dictogram(object):

	def __init__(self, corpus=None):
		# super(Dictogram, self).__init__()
		self.corpus = corpus
		self.corpus_list = self.corpus.lower().split()
		self.histogram = self._dict_histogram()
		self.tokens = len(self.corpus_list)

	def _dict_histogram(self):
		"""
	        This creates a Dictogram with a source text.
		"""
		histogram = {}
		for word in self.corpus_list:
			if word in histogram:
				histogram[word] += 1
			else:
				histogram[word] = 1
		return histogram

	def frequency(self, word):
    	# check if the word input is in the dictionary
		if word in self.histogram:
        	# if so return the value
			return self.histogram[word]

	def probabilities_frequency(self, word):
	    # call the frequency_word function and
		# allow of the int to be a float
		frequency = float(self.frequency(word))
	    # return the result
		return frequency / self.tokens

	# Step 4. Dictogram
	def random_word(self):
		"""
		Stochastic Sampling for dictionaries.
		"""
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
    file_corpus = "One dog two dog red dog blue dog"
    test = Dictogram(file_corpus)
    print(test.histogram)
    print(test.tokens)
    print(test.random_word())
