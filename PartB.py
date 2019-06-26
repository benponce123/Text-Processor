# CS 121
# Assignment 1 - Text Processing Functions
# Part B
# Benjamin Ponce 85348479


import sys
import PartA


# Counts the number of words that the two files have in common
# Returns an integer with the number of common words
# O(n) - runs in linear time because each word n in the dictionary is visited
def count_tokens(dict1, dict2):
    count = 0
    for word in dict1:
        if word in dict2:
            count += 1
    return count


# Calls other functions including functions from PartA.py
# Displays the output
# O(n) - runs in linear time because each line n is read
def display_output():
    dict1 = {}
    dict2 = {}
    for line1 in PartA.get_line(1):
        tokens1 = PartA.tokenize_text(line1)
        words_dict1 = PartA.count_words(tokens1, dict1)
    for line2 in PartA.get_line(2):
        tokens2 = PartA.tokenize_text(line2)
        words_dict2 = PartA.count_words(tokens2, dict2)
    print(count_tokens(dict1, dict2))
    

if __name__ == '__main__':
    display_output()


