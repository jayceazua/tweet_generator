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
