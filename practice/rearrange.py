import random


"""
function shuffle(array) {
  var m = array.length, t, i;

  // While there remain elements to shuffle…
  while (m) {

    // Pick a remaining element…
    i = Math.floor(Math.random() * m--);

    // And swap it with the current element.
    t = array[m];
    array[m] = array[i];
    array[i] = t;
  }

  return array;
}
"""

def rearrange_words(sentence): # Fisher-Yates Shuffle Implemented.
    sentence_length = len(sentence) - 1 # get the length of the sentence being passed
    for i in range(sentence_length, 0, -1): # range(start, stop, step) in this case backwards
        random_num = random.randint(0, i) # generates random number
        if random_num == i:
            continue
        # swap it index of words around - trade places
        sentence[i], sentence[random_num] = sentence[random_num], sentence[i]
    return sentence



def main():
    words_list = "Would I rather be feared or loved? Easy. Both. I want people to be afraid of how much they love me.".split()
    print(rearrange_words(words_list))


if __name__ == "__main__":
    main()
