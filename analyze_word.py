def get_words(source_text):
    words = source_text.lower().split()
    return words



# Dictionary Historgram Function
def dict_histogram(source_text):
    words = get_words(source_text)
	# declare an empty dictionary
    histogram = {}
	# loop into the list
    for word in words:
		# if the word is in the list_sen
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram


# 1. What is the least/most frequent word(s)?
# 2. How many different words are used?
# 3. What is the average (mean/median/mode) frequency of words in the text?

# run the code
if __name__ == "__main__":
    file = "One fish two fish red fish blue fish"
    print(dict_histogram(file))
