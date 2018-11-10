import sys

file = "One fish two fish red fish blue fish"


# List of Lists Histogram Function
def list_histogram(source_text):
	source_txt = source_text.lower()
	# turn the source_text from a string into a list
	list_sen = source_txt.split()
	# declare an empty list
	histogram = []

	# histogram = [['one', 1], ['fish', 4], ['two', 1], ['red', 1], ['blue', 1]]



# Dictionary Historgram Function
def dict_histogram(source_text):
	# declare an empty dictionary
	histogram = {}
	# split the sentence from above into a list
	list_sen = source_text.lower().split()
	# loop into the list
	for word in list_sen:
		# if the word is in the list_sen
		if word in histogram:
			# add one into that key
			histogram[word] += 1
		else:
			# if is not create a key with the value of 1
			histogram[word] = 1
	return histogram


# 1. What is the least/most frequent word(s)?
# 2. How many different words are used?
# 3. What is the average (mean/median/mode) frequency of words in the text?

# run the code
if __name__ == "__main__":
	print(dict_histogram(file))
