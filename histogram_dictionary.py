"""
Visualizing histogram.
original_str = 'one fish two fish three fish four fish'
dict_histogram_of_original_str = {one: 1, fish: 4, two: 1, three: 1, four: 1}
"""

class Histogram():


    def __init__(self, str_words) -> None:
        """Initialize histogram with words given"""
        self.str_words = str_words
        self.histogram = self.get_histogram()

    def get_histogram(self) -> dict:
        '''Dictionary histogram'''
        # initialize my variables
        dict_histogram = {}
        # receive a string and split it to create an array
        arr_words = self.str_words.split()
        # iterate array
        for word_indexed in arr_words:
            # condition plus one each repeated word
            if word_indexed not in dict_histogram:
                # add new word to dictionary
                dict_histogram[word_indexed] = 1
            else:
                # increment counter for words that already exist
                dict_histogram[word_indexed] += 1
        return dict_histogram


    def get_unique_words(self) -> int:
        return len(self.histogram)


    def get_frequency(self, find_word: str) -> int:
        return self.histogram[find_word] if find_word in self.histogram else 0


def main():
    pass 




if __name__ == "__main__":
    main()
