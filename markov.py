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

    split_corpus = corpus.split()

    # print split_corpus

    for i in range(len(split_corpus) - n):
        words = []
        # words = (words,) * n
        words.extend(split_corpus[i : i + n])

        words_as_a_tuple = tuple(words)

        # for counter in range(n):
        #     words.append = split_corpus[i + counter]         

        next_word = split_corpus[i + n]
        # pair_of_words = (split_corpus[i], split_corpus[i + (n - 1)])
        # third_word = split_corpus[i + n]
        if not d.get(words_as_a_tuple):
            d[words_as_a_tuple] = [next_word]
        else: 
            d[words_as_a_tuple].append(next_word)

    # print d
    return d

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    # create list of keys that start with capitalized word
    capitalized_keys = []
    endpunct_keys = []
    for i in range(len(chains.keys())):
        if ord(chains.keys()[i][0][0]) in range(65, 91):
            capitalized_keys.append(chains.keys()[i])
        elif ord(chains.keys()[i][-1][-1]) in [33, 34, 46, 63]:
            endpunct_keys.append(chains.keys()[i])

    # print endpunct_keys
    # print capitalized_keys
    # kick off loop with random selection in dictionary
    kickoff_key = random.choice(capitalized_keys)
    # print ""
    # print kickoff_key

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

    
    # return "Here's some random text."

def main():
    args = sys.argv
    # The command exists returns True if a file exists, based on its name in a string as an argument. 
    # It returns False if not.
    from os.path import exists

    # Takes in Python script and one file as arguments. 
    script, input_file1, input_file2 = args
    isValid = True

    # Check if input_file exists.
    if not exists(input_file1):
        print "%r does not exist!" % input_file1
        isValid = False
    elif not exists(input_file2):
        print "%r does not exist!" % input_file2
        isValid = False

    if isValid:
        # open and read file
        f1 = open(input_file1)
        f2 = open(input_file2)

        input_text1, input_text2 = '', ''

        for i in xrange(700):
            input_text1 += f1.readline()
            input_text2 += f2.readline()
            # print input_text1, input_text2

        input_text = input_text1 + input_text2
        # print input_text
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



