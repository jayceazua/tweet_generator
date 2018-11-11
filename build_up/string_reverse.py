# declaring a function with a param
def reverse_word(input_word):
    reversed_word = ""
    for i in range(0, len(input_word)):
        # Get the last index of the string and concats it to the empty string above
        reversed_word += input_word[len(input_word) - 1 - i]
    return reversed_word

def reverse_sentences(input_sentence):
    # spliting the sentence per word into a list
    reverse_sentence = ""
    for i in range(0, len(input_sentence)):
        reverse_sentence += input_sentence[len(input_sentence) - 1 - i]
    return reverse_sentence.strip()

def main():
    word = "LOVE"
    original_words = quotes = "Would I rather be feared or loved? Easy. Both. I want people to be afraid of how much they love me."
    print(reverse_word(word))
    print('--------')
    print(reverse_sentences(original_words))

if __name__ == "__main__":
	# this calls the function made above
    main()
