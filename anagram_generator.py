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
    word = "war"
    print(anagram(word))

if __name__ == "__main__":
    main()
