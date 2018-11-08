def all_perms(elements):
   if len(elements) <= 1:
       return elements
   else:
       possible_words = []
       for perm in all_perms(elements[1:]): # using the power of recursion
           for i in range(len(elements)): # loop obvs lol
               possible_words.append(perm[:i] + elements[0:1] + perm[i:])
       return possible_words

def main():
    word = "war"
    print(all_perms(word))

if __name__ == "__main__":
    main()
