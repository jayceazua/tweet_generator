"""
Improvements:
        - If i input 'tree' it duplicates the possbilities for one more iteration.
        - Need to create a good error handling for dubplicates and not be able to append it,
            into the return list of possible words.
"""


def anagram(word):
   if len(word) <= 1:
       return word
   else:
       possible_words = []
       for perm in anagram(word[1:]): # using the power of recursion
           for i in range(len(word)): # loop obvs lol
               possible_words.append(perm[:i] + word[0:1] + perm[i:])
       return possible_words

def main():
    word = "tree"
    print(anagram(word))

if __name__ == "__main__":
    main()
