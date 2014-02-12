#!/usr/bin/env python

import sys
#TO-DO:  is this the same as saying "from sys import *"?

import random

#COMMENT: get raw input from user for n grams. (this was originally in make_chains() function)
n = int(raw_input("How many n's in your grams? > "))

#COMMENT: get raw input of length of Markov string requested (this was originally in make_text() function)
x = int(raw_input("How many words would you like in your text? > "))
    # TO-DO QUESTION A: Can I set x and n above as global variables so can be referenced in both fucntions
    #    or can/should I put in MAIN function? Is there a better way so I'm not using global variables?
    #   (That way I can reference n by typing x-n and then range(x-n) below to get the actual correct # of 
    #   words requested by user input) - See TODO Question B below



def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    #COMMENT: Take text_body and split into list of words by white space
    word_list = corpus.split()
    # print word_list

    #COMMENT: loop through to create dictionary key of n-gram strings: paired with next word
    markov_dict = {}
    for i in range(len(word_list) - n):
        markov_dictkey = " ".join(word_list[i:i+n]) 
        # print markov_dictkey
        if markov_dict.get(markov_dictkey) is not None:
           markov_dict[markov_dictkey].append(word_list[i+n]) 
        else: 
            markov_dict[markov_dictkey] = [word_list[i+n]]
# TO-DO: QUESTION: keep count of each instance of the value for a specific markov_dict key instead and use probability #'s?

    # print markov_dict    
    return markov_dict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""


    markov_string = random.choice(chains.keys())

    # COMMENT Take the start key and choose randomly from associated values
    new_word = random.choice(chains[markov_string])
    # print "this is your start string: ", markov_string
    # print "this is the word to be added to the string: ", new_word

    for i in range(x-n):
        # COMMENT append word to exxisting string
        markov_string += ' ' + new_word
        # COMMENT Take the existing string and split into list temporarily
        markov_string_list = markov_string.split()
        # COMMENT join the last n items as new look up key
        new_key = " ".join(markov_string_list[-n:])
        # COMMENT use new look up key to find associated values to choose randomly from
        new_word = random.choice(chains[new_key])

    return markov_string
    # print "your markov_string is: ", markov_string

def main():
    # COMMENT allows unspecified number of files to mash together
    args = sys.argv

    # COMMENT loops through and combines all the text files into one string in input_text
    input_text = ""
    for i in range(1,len(args)):
        f = open(args[i])
        input_text += f.read() + ' '

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()


# TO-DO LIST
# Create a new Twitter persona and wire up your markov program with the twitter module (import twitter) to produce random tweets.

# Do the checks for capital letters and end puncutation
# Put in check if input file exists and return message if not

# check against markov.py methodology
