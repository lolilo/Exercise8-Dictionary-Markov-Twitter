#!/usr/bin/env python

import sys
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    #COMMENT: Take text_body and split into list of words by white space
    word_list = corpus.split()
    # print word_list

    #COMMENT: get raw input from user for n grams
    n = int(raw_input("How many n's in your grams? >"))

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

    x = int(raw_input("length of your sentence? >"))
    # TO-DO QUESTION: If wanted to, could I set this and n above as global variables and then reference 
    #   them from inside the function? That way I can reference n by typing x-n and then range(x-n) below
    #   to get the actual correct # of words requested by user input

    markov_string = random.choice(chains.keys())
    # print start_key
    for i in range(x):
        new_word = random.choice(chains[markov_key])
        markov_string += ' ' + random.choice(chains[markov_key])


        # Take the start key and look up associated values to choose randomly from
        # concatenate start key with random value
        # Take the existing string and split into list temporarily, join the last n items as new look up key
        # use new look up key to find associated values to choose randomly from

        start_key = 

    return "Here's some random text."
    # return markov_string

def main():
    script, firstfile  = sys.argv

    #COMMENT: Change this to read input_text from a file
    f = open("test.txt")
    input_text = f.read()
    # print input_text

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()


# TO-DO LIST
# Put in check if input file exists to give feedback
# How would you have an unlimited number of argv that you could input from command line? 

# put in two files or more
# check against markov.py methodology
# Create a new Twitter persona and 
#   wire up your markov program with the twitter module (import twitter) to produce random tweets.