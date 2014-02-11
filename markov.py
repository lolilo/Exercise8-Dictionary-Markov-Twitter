#!/usr/bin/env python

import sys
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    # n-gram Markov chains
# TO-DO:    n = 2

    d = {}

    split_corpus = corpus.split()

    # print split_corpus

    for i in range(len(split_corpus) - 2):
        pair_of_words = (split_corpus[i], split_corpus[i + 1])
        third_word = split_corpus[i + 2]
        if not d.get(pair_of_words):
            d[pair_of_words] = [third_word]
        else: 
            d[pair_of_words].append(third_word)

    # print d
    return d

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

# kick off loop with random selection in dictionary
    kickoff_key = random.choice(chains.keys())
    # print ""
    # print kickoff_key

# from that key, chose random value
    markov_string = kickoff_key[0] + ' ' + kickoff_key[1]
    for i in range(20):
        if not chains.get(kickoff_key):
            continue
        else: 
            next_word = random.choice(chains[kickoff_key]) 
            # print next_word
            kickoff_key = kickoff_key[1], next_word
            markov_string += ' ' + next_word

            # print kickoff_key
            # print ""
    return markov_string
# append to string 
# chain value with previous word to create key for next loop
# specify how many iterations 

    
    # return "Here's some random text."

def main():
    args = sys.argv
    # The command exists returns True if a file exists, based on its name in a string as an argument. 
    # It returns False if not.
    from os.path import exists

    # Takes in Python script and one file as arguments. 
    script, input_file = args
    isValid = True

    # Check if input_file exists.
    if not exists(input_file):
        print "%r does not exist!" % input_file
        isValid = False

    if isValid:
        # open and read file
        f = open(input_file)
        input_text = f.read()

        chain_dict = make_chains(input_text)
        # print chain_dict
        random_text = make_text(chain_dict)
        print random_text

if __name__ == "__main__":
    main()



