#!/usr/bin/env python

import sys
import random

# After Liz's code review:
# Edit code such that it returns an actual sentence with first word capitalized
# ending with end punctuation.

# edit kickoff_key such that it always starts with capitalized word
# somehow end with punctuation


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    # n-gram Markov chains
    n = 2
    d = {}

    # break up .txt string into list of words
    split_corpus = corpus.split()

    # len(split_corpus) - n  ~ - n to not account for very last word. 
    for i in range(len(split_corpus) - n):
        words = []
        # make an n-gram as a list
        words.extend(split_corpus[i : i + n])
        # convert list into a tuple, in order to use them as key in dict
        # only immutable data types for keys!
        words_as_a_tuple = tuple(words)     

        # assign variable to find the next word
        # this will be the dict value for the tuple key
        next_word = split_corpus[i + n]

        # populate dictionary
        if not d.get(words_as_a_tuple):
            d[words_as_a_tuple] = [next_word]
        else: 
            d[words_as_a_tuple].append(next_word)

    capitalized_keys = []
    endpunct_keys = []
    for i in range(len(d.keys())):
        if ord(d.keys()[i][0][0]) in range(65, 91):
            capitalized_keys.append(d.keys()[i])
        elif ord(d.keys()[i][-1][-1]) in [33, 34, 46, 63]:
            endpunct_keys.append(d.keys()[i])

    print d
    print capitalized_keys
    print endpunct_keys
    return d, capitalized_keys, endpunct_keys

    # should we create a separate dictionary for capitlized things/end punc or just
    # new lists to select from one master dictionary? 
    # The two lists method is better. Make sure you only create the two lists once! 

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    # create list of keys that start with capitalized word
    

    # print endpunct_keys
    # print capitalized_keys
    # kick off loop with random selection in dictionary
    kickoff_key = random.choice(capitalized_keys)

    length_of_sentence = 20
# from that key, chose random value
    markov_string = kickoff_key[0] + ' ' + kickoff_key[1]
    
    for i in range(length_of_sentence):
        if not chains.get(kickoff_key):
            continue
        elif markov_string[-1] in [33, 34, 46, 63]:
            next_word = random.choice(capitalized_keys)[0]            
        elif i == length_of_sentence - 1:
            # print endpunct_keys
            next_word = random.choice(endpunct_keys)[1]
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

def main():
    args = sys.argv
    # The command exists returns True if a file exists, based on its name in a string as an argument. 
    # It returns False if not.
    from os.path import exists

    # Takes in Python script and one file as arguments. 
    script, input_file1 = args
    isValid = True

    # Check if input_file exists.
    if not exists(input_file1):
        print "%r does not exist!" % input_file1
        isValid = False
    # elif not exists(input_file2):
    #     print "%r does not exist!" % input_file2
    #     isValid = False

    if isValid:
        # open and read file
        f1 = open(input_file1)
        # f2 = open(input_file2)

        input_text1 = ''

        for i in xrange(700):
            input_text1 += f1.readline()
            # input_text2 += f2.readline()
            # print input_text1, input_text2

        input_text = input_text1 
        chain_dict = make_chains(input_text)
        # print chain_dict
        random_text = make_text(chain_dict)
        random_text1 = make_text(chain_dict)
        random_text2 = make_text(chain_dict)
        random_text3 = make_text(chain_dict)
        print random_text
        print random_text1
        print random_text2
        print random_text3

if __name__ == "__main__":
    main()



