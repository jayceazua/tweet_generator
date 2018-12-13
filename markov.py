import random
import re


########## ########## ########## ##########
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
	def random_word(self, histogram):
		"""
		Stochastic Sampling for dictionaries.
		"""
	    # generate a random float integer from 0 to 1
		random_num = random.uniform(0, 1)
	    # this variable is used to update as we loop
		running_total = 0.0
	    # loop through the dictionary histogram
		for key, value in histogram.items():
	        # runs the probabilities_frequency function and adds it to the running_total variable
			running_total += self.probabilities_frequency(key)
	        # if the running_total variable is equal to our greater than the random_num
			if running_total >= random_num:
	            # return the current key of the loop it is in and break out of it
				return key

	def get_words(self): # this is where I clean the corpus
	    """ Opens the file and split it into a list """
	    with open(self.corpus) as dictionary_file:
	        dictionary_words = dictionary_file.read().replace("\n", "")
	    # cleanup.py might come here.
	    return dictionary_words.split(' ')


	def generate_sentence(self, list_words): # generates sentences but no markov
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

	def markov_dict(self, tokens):
	    markov_dict = {}
	    for index, token_key in enumerate(tokens):
	        if index == len(tokens) - 1: break
	        if token_key not in markov_dict:
	            markov_dict[token_key] = {tokens[index + 1]: 1}
	        else:
	            next_token = tokens[index + 1]
	            if next_token not in markov_dict[token_key]:
	                markov_dict[token_key][next_token] = 1
	            else:
	                markov_dict[token_key][next_token] += 1
	    return markov_dict

	def tweet_generator(self, markov_dict):
		# empty list or sentenve varliable to push
		temp_markov_sentence = []
		# TODO: random walk function <-- 1. random choice from the markov_dict (random key)
		# pull a random word within the key "random sample of the values"
		# TODO:
		pass

if __name__ == "__main__":
	test = Dictogram('test_corpus.txt')
	# print(test.random_word(test.histogram))
	markov = test.markov_dict(test.corpus_list)
	print(test.random_word(markov['A']))

"""{
'A': {'man,': 1, 'dog,': 1},
'man,': {'a': 1},
'a': {'plan,': 1, 'canal:': 1, 'panic': 1, 'pagoda!\n': 1},
'plan,': {'a': 1},
'canal:': {'Panama!': 1},
'Panama!': {'A': 1},
'dog,': {'a': 1},
'panic': {'in': 1},
'in': {'a': 1}
}

2. markov[state_from_before]

 """