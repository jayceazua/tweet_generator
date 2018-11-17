# module for generating a sentence from a histogram
def random_words_arrange(input_int, list_words):
	"""
	This function uses the words from a file
		and generates a random "sentence"
	"""
	# I am getting the total length of the file.
	len_file = len(get_words())
	# declare an empty list
	words_list = []
	# stores the sentence here
	sentence = ""
		# the condition is when
	while input_int != 0:
		# generates a random number based on the length of the file
		rand_num = random.randint(0, len_file)
		# it will add the random selected word into our empty list
		words_list.append(list_words[rand_num] + " ")
		# prevents from getting the same word
		list_words.pop(rand_num)
		# subtract by one to loop again
		input_int -= 1
	return sentence.join(words_list)
