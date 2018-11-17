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

class Dictogram(dict):

	def __init__(self, corpus=None):
		super(Dictogram, self).__init__()
		self.corpus = corpus
		self.corpus_list = self.get_words() # cleanup.py
		self.histogram = self._dict_histogram()
		self.tokens = len(self.corpus_list) # word_count.py

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

	def get_words(self):
	    """ Opens the file and split it into a list """
	    with open(self.corpus) as dictionary_file:
	        dictionary_words = dictionary_file.read()
	    # cleanup.py might come here.
	    return dictionary_words.split(' ')

	def generate_sentence(self, list_words):
		"""
		This function uses the words from a file
			and generates a random "sentence"
		"""
		# declare an empty list
		words_list = []
		# stores the sentence here
		sentence = ""
		input_int = random.randint(5, 10)
			# the condition is when
		while input_int != 0:
			words_list.append(self.random_word() + " ")
			input_int -= 1
		return sentence.join(words_list)


if __name__ == "__main__":
	test = Dictogram('test_corpus.txt')
	print(test.generate_sentence(test.corpus_list))
