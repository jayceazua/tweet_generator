from histogram import Dictogram

file_corpus = "One dog two dog red dog blue dog"
test = Dictogram(file_corpus)
print(test.histogram)
print(test.tokens)
print(test.random_word())
