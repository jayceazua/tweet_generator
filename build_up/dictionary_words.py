import random
import sys


def get_words():
    """ Opens the file and split it into a list """
    with open('/usr/share/dict/words') as dictionary_file:
        dictionary_words = dictionary_file.read()
    # split('\n') returns the last index of the list with a empty string
    # use splitlines() to now allow that.
    return dictionary_words.splitlines()

def user_input():
    """ Make sure that the user is putting in an integer """
    user_input = sys.argv[1]
    if type(user_input) != 'int':
        return 'Invalid Input; please input a integer.'
    else:
        return user_input

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
		rand_num = random.randint(0, len_file -1)
		# it will add the random selected word into our empty list
		words_list.append(list_words[rand_num] + " ")
		# prevents from getting the same word
		list_words.pop(rand_num)
		# subtract by one to loop again
		input_int -= 1
        # avoids index out-of-bounds
		len_file -= 1

	return sentence.join(words_list)

def main():
    list_words = get_words()
    input_int = int(sys.argv[1])
    print(random_words_arrange(input_int, list_words))

if __name__ == "__main__":
    main()
