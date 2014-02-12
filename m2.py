#!/usr/bin/env python

import sys
#TO-DO:  is this the same as saying "from sys import *"?

import random

from os.path import exists

def make_chains(corpus, n):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    #COMMENT: Take text_body and split into list of words by white space
    word_list = corpus.split()
    # print word_list

    #COMMENT: loop through to create dictionary key of n-gram strings: paired with next word
    markov_dict = {}

    for i in range(len(word_list) - n):

        markov_dictkey =  tuple(word_list[i : i + n]) #" ".join(word_list[i:i+n]) 
        # print markov_dictkey

        if markov_dict.get(markov_dictkey):
           markov_dict[markov_dictkey].append(word_list[i + n]) 
        else: 
            markov_dict[markov_dictkey] = [word_list[i + n]]
# TO-DO: QUESTION: keep count of each instance of the value for a specific markov_dict key instead and use probability #'s?

    # print markov_dict    
    return markov_dict

def capital_start(markov_dict):
    capitalized_keys = []
    for i in range(len(markov_dict.keys())):  
        if ord(markov_dict.keys()[i][0][0]) in range(65, 91):
            capitalized_keys.append(markov_dict.keys()[i])
    return capitalized_keys

def end_punct(markov_dict):
    endpunct_keys = []
    for i in range(len(markov_dict.keys())):
        if ord(markov_dict.keys()[i][-1][-1]) in [33, 34, 46, 63]:
            endpunct_keys.append(markov_dict.keys()[i])
    return endpunct_keys

# takes in a dictionary, list of capital keys, list of end keys, n = n-gram, x = max # characters
# returns string
def make_text(chains, cap_keys, end_keys, n, x):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    key = random.choice(cap_keys)
    # COMMENT Take the start key and choose randomly from associated values

    # print "this is your start string: ", markov_string
    # print "this is the word to be added to the string: ", new_word
    markov_string = ''
    # convert tuple key into a string
    for word in range(len(key)):
        markov_string += key[word] + ' '


    while len(markov_string) < x:
    # for i in range(x - n):
        # checks to make sure not final key so as to get next word that does not exist

        if not chains.get(key):
            key = random.choice(chains.keys())

        if key in end_keys:
            break
        # if key in end_keys:
        #     key = random.choice(cap_keys)    
        # if sentence_checker(markov_string): #key in end_keys:
        #     return markov_string
            # break
        # COMMENT append word to existing string
            
        # To-Do check with Nick if this is avoiding list concatenation issue
        # compare this part to m.py
        new_word = random.choice(chains[key])
        markov_string += new_word + ' '
        # print i, markov_string
        # print ''
        # COMMENT Take the existing string and split into list temporarily
        # markov_string_list = markov_string.split()
        # COMMENT join the last n items as new look up key

        new_key_list = list(key[1:])
        # print i
        new_key_list.append(new_word) # " ".join(markov_string_list[-n:])
        key = tuple(new_key_list)
        
        # COMMENT use new look up key to find associated values to choose randomly from

    return markov_string
    # print "your markov_string is: ", markov_string

# takes in sentence and checks for end punctuation
def sentence_checker(sentence):
    # print sentence[-1]
    if sentence[-2] in ['!', '?', '.', '~']:
        return True
    else:
        return False

def main():
    # COMMENT allows unspecified number of files to mash together
    args = sys.argv
    # Ensure user inputs at least one text file
    isValid = True

    if len(args) < 2:
        print "Please provide at least one .txt file."
        isValid = False

    # Check if args exists
    for f in args:
        if not exists(f):
            print "%r does not exist!" % f
            isValid = False

    # COMMENT loops through and combines all the text files into one string in input_text
    if isValid:

        #COMMENT: get raw input from user for n grams. (this was originally in make_chains() function)
        n = int(raw_input("How many n's in your grams? > "))

        #COMMENT: get raw input of length of Markov string requested (this was originally in make_text() function)
        x = int(raw_input("What is the maximum number of characters in your text? > "))

        input_text = ""
        for i in range(1,len(args)):
            f = open(args[i])
            for j in xrange(200):
                input_text += f.readline()

        chain_dict = make_chains(input_text, n)
        # for i in chain_dict.items():
        #     print i
        # print chain_dict
        cap_keys = capital_start(chain_dict)
        end_keys = end_punct(chain_dict)

        # TEST: test for capital and puncutation functions
        # print cap_keys
        # print end_keys

        random_text = 'Beginning text'
        while not sentence_checker(random_text):
            # print random_text[-2]
            # print sentence_checker(random_text)
            # print random_text
            random_text = make_text(chain_dict, cap_keys, end_keys, n, x)
        print random_text

if __name__ == "__main__":
    main()


# TO-DO LIST
# Create a new Twitter persona and wire up your markov program with the twitter module (import twitter) to produce random tweets.

# Do the checks for capital letters and end puncutation
# Put in check if input file exists and return message if not

# check against markov.py methodology
