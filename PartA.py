# CS 121
# Assignment 1 - Text Processing Functions
# Part A
# Benjamin Ponce 85348479


import sys
import re


# Opens and reads the file line by line
# Yield is used so that the entire text is not stored in memory
# Yields line to perform actions on it and after resumes on the next line
# O(n) - runs in linear time because of n many lines in the text file
def get_line(file):
    with open(sys.argv[file]) as file:
        for line in file:
            yield line
    

# Substitutes the non-alphanumeric characters with a space,
#   and splits the words into a list
# Returns a list containing the tokens from the text
# O(n) - runs in linear time because each character n is checked
#   if they are alphanumeric characters
def tokenize_text(text):
    new_text = re.sub('[^ a-zA-Z0-9]', ' ', text.lower())    
    return new_text.split()


# Counts the frequency of each token from the text
# Returns a dictionary with the tokens as keys and frequencies as values
# O(n) - runs in linear time because each token n in the list is visited
def count_words(tokens, words_dict):    
    for word in tokens:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    return words_dict


# Sort key to sort the list by the frequency
# Returns the second element in the tuple
# O(1) - runs in constant time because it returns the index
def sort_frequency(x):
    return x[1]


# Prints each token and frequency
#   sorted by the highest frequency and alphabetically
# O(n log n) - runs in log-linear time because of sorting
def print_word_frequency(words_dict):    
    word_freq = list(words_dict.items())
    word_freq.sort()
    word_freq.sort(key = sort_frequency, reverse = True)
    for x in word_freq:
        print(str(x[0]) + "\t" + str(x[1]))


# Calls other functions to display the final output
# O(n) - runs in linear time because each line n is read
def display_output():
    words_dict = {}
    for line in get_line(1):
        tokens = tokenize_text(line)
        words_dict = count_words(tokens, words_dict)
    print_word_frequency(words_dict)
     

if __name__ == '__main__':
    display_output()



