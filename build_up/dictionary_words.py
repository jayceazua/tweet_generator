import sys
import random

def read_file(file):
    file_read = open(file, 'r')
    corpus = file_read.read().splitlines()
    file_read.close()
    return corpus

def random_sentence(corpus, num):
    sentence = []
    while num != 0:
        random_index = random.randint(0, len(corpus) - 1) # random walk?
        sentence.append(corpus[random_index])
        # prevents from selecting the same word
        corpus.pop(random_index)
        num -= 1
    return ' '.join(sentence)

if __name__ == "__main__":
    num = sys.argv[1:]
    num = int(num[0])
    file = "/usr/share/dict/words"
    corpus = read_file(file)
    print(random_sentence(corpus, num))
