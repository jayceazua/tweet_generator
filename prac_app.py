# main script, uses other modules to generate sentences
import word_frequency
import cleanup
import markov



    # Get cleaned data
file_name = 'test_corpus.txt'
cleaned_file = cleanup.clean_file(file_name)
    # Create data structure
data_structure = markov.make_higher_order_markov_model(2, cleaned_file)
    # Pass data structure to get random setence with 140 chars
random_sentence = markov.generate_random_sentence_n(50, data_structure)

print(random_sentence)
