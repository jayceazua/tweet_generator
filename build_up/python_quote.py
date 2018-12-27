import random

def random_python_quote(quotes):
    rand_index =  random.randint(0, len(quotes) - 1)
    return quotes[rand_index]

if __name__ == "__main__":
    quotes = ("It's just a flesh wound.",
              "He's not the Messiah. He's a very naughty boy!",
              "THIS IS AN EX-PARROT!")
    quote = random_python_quote(quotes)
    print(quote)
