# Python Specs
import random

quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")

def random_python_quote():
    rand_index = random.randint(0,len(quotes) -1)
    return quotes[rand_index]

# Question 1
st = "Print only the words that start with s in this sentence"

for word in st.split():
    if word[0] == 's':
        print(word)

# Question 2
# 'Use rang() to print all the even numbers from 0 to 10'
# range(start, end, space)
print(range(0, 11, 2))

# Question 3
# 'Use List Comprehension to create a list of all numbers between 1 and 50 that are divisble by 3'
x = [n for n in range(1, 50) if n % 3 == 0]
print(x)

# Question 4
# 'Go through the string below and if the length of a word is even print "even!"'
st = "Print every word in this sentence that has an even number of letters"
for word in st.split():
    if len(word) % 2 == 0:
        print(word + ' <-- has an even length!')

# Question 5

for n in range(1, 101):
    """
    Write a program that prints the integers from 1 to 100.
    But for multiples of 3 print "Fizz" instead of the number, and for the
    multiples of 5 print "Buzz". For numbers which are multiples of both 3
    and 5 print "FizzBuzz".
    """
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 5 == 0:
        print('Buzz')
    elif n % 3 == 0:
        print('Fizz')
    else:
        print(n)

# Question 6
# 'Use List Comprehension to create a list of the letters of every word in the string'
st = 'create a list of the letters of every word in the string'
lst = [word[0] for word in st.split()]
print(lst)

def is_prime(num):
    # this is a docstring
    """
    INPUT: A number
    OUTPUT: A statement whether or not a number is a prime
    """
    for n in range(2, num):
        if num % n == 0:
            print('Not prime')
            break
    else:
        print('The number is prime!')


# lambda expressions allow to create anonymous functions
# able to quickly make ad-hoc functions without needing to properly define them
# coding simple functions
# lambda is for a quick anonymous function
def square(num):
    results = num **2
    return result

def square(num):
    return num ** 2

def square(num): return num ** 2

lambda num: num ** 2
square = lambda num: num**2
# check number is even
even = lambda num: num % 2 == 0
print(even(4))
# usually used in map, filter, reduce methods

mod = lambda num: num % 2 ** 4
print(mod(4))


# #################### #

# Q 1: Write a function that computes the volume of a sphere given its radius
def vol(rad):
    rad_cubed = rad**3
    four_one_thirds = 1.33333333333
    pi = 3.14159265359
    vol = four_one_thirds * pi * rad_cubed
    return vol


# Q 2: Write a function that checks whether a number is in a given range
# inclusive of high and lower -
def ran_check(num, low, high):
    pass

# Q 2.5: If you wanted to return a boolean
def ran_bool(num, low, high):
    pass
# ran_bool(3, 1, 10) # OUTPUT: True

# Q 3: Write a Python function that accepts a string and calculates the number
# upper case letters and lower case letters
# Sample String: 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected OUTPUT:
# No. of Upper case characters: 4
# No. of Lower case characters: 33
# Explore the collections module to solve this problem
def up_low(str):
    pass

# Q 4: Write a Python function that takes a list and returns a new list with
# unique elements of the first list
# Sample list: [1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5]
# Unique list: [1, 2, 3, 4, 5]
def unique_list(lst):
    pass

# Q 5: Write a python function to multiply all the numbers in a list
# Sample list: [1, 2, 3, -4]
# OUTPUT: -24



# Q 6: Write a python function that checks whether a passed string is
# palindrome or Not
# A palindrome is word,phrase, or sequence that reads the same backward as forward
def palindrome(str):
    pass

# HARD Q 7: Write a python function to check whether a string is a pangram or not
# Pangrams are words or sentences containing every letter or the alphabet at least once
# INPUT: "The quick brown fox jumps over the lazy dog"
import string

def isPangram(str1, alphabet=string.ascii_lowercase):
    pass



# a conditional that will only run certain code if the current process file is the current source file
# if __name__ == "__main__":
