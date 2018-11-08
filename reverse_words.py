import sys

original_words = quotes = "Would I rather be feared or loved? Easy. Both. I want people to be afraid of how much they love me."

# turn the above into a reusable func

# declaring a function with a param
def reverse_words_quote(input_words):
	# takes in a string and splits it up
	# into a list and stores it in a var
	sentence = input_words.split()
	# takes in the list created above then
	# starts from the end of the list and reverses it
	sentence_rev = sentence[::-1]
	#  from the reversed list it joins it back
	# together with a space " " in between
	sen_rev = " ".join(sentence_rev)
	 # returns the above variable
	return sen_rev


if __name__ == "__main__":
	# this calls the function made above
	quote = reverse_words_quote(original_words)
	print(quote)
