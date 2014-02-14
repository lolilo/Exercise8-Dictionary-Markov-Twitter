#!/usr/bin/env python

# https://code.google.com/p/python-twitter/
# dev.twitter.com

# API - application programming interface

import sys
import random
from os.path import exists


import twitter
import os
# tweet on Twitter from command line
def tweet(tweettext):
    # key encryption
    twitter_key0 = os.environ.get("TWITTER_API_KEY")
    twitter_key1 = os.environ.get("TWITTER_API_SECRET")
    twitter_key2 = os.environ.get("TWITTER_ACCESS_TOKEN")
    twitter_key3 = os.environ.get("TWITTER_ACCESS_SECRET")

    api = twitter.Api(consumer_key=twitter_key0,
                      consumer_secret=twitter_key1,
                      access_token_key=twitter_key2,
                      access_token_secret=twitter_key3)

    status = api.PostUpdate(tweettext)

def make_chains(corpus, n):
    """Takes an input text as a string, and returns a dictionary of
    n-gram markov chains."""

    # split string corpus by white space into a list of strings
    word_list = corpus.split()
    markov_dict = {}

     # loop through to create dictionary key of n-gram strings: paired with next word
    for i in range(len(word_list) - n):

        markov_dictkey =  tuple(word_list[i : i + n]) 
        
        if markov_dict.get(markov_dictkey):
           markov_dict[markov_dictkey].append(word_list[i + n]) 
        else: 
            markov_dict[markov_dictkey] = [word_list[i + n]]

    return markov_dict

# takes in a dictionary and returns a list of all capitlized keys in the dictionary
def capital_start(markov_dict):
    capitalized_keys = []
    for i in range(len(markov_dict.keys())):  
        first_letter = markov_dict.keys()[i][0][0]
        if ord(first_letter) >= ord('A') and ord(first_letter) <= ord('Z'): # ord(char) more readable than straight-up ord numbers
            capitalized_keys.append(markov_dict.keys()[i])
    return capitalized_keys

# takes in a dictionary and returns a list of all keys with end punctuation
def end_punct(markov_dict):
    endpunct_keys = []
    for i in range(len(markov_dict.keys())):
        if ord(markov_dict.keys()[i][-1][-1]) in ['!', '?', '.', '~']: # strings are more readable than ASCII ordinal numbers
            endpunct_keys.append(markov_dict.keys()[i])
    return endpunct_keys

# takes in a dictionary, list of capital keys, list of end keys, n = n-gram, x = max # characters desired in markov string
# returns markov string
def make_text(chains, cap_keys, end_keys, n, x):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    # to start off the algorithm, choose a random key from the list of capitalized keys
    key = random.choice(cap_keys)

    # print "this is your start string: ", markov_string
    # print "this is the word to be added to the string: ", new_word
    markov_string = ''
    # convert tuple key into a string and add it to the markov string
    for word in range(len(key)):
        markov_string += key[word] + ' '

    while len(markov_string) < x - 10:
    # for i in range(x - n):
        # if key is not in dictionary (this happens if we create a key from the last set of words in the provided text), choose another key
        if not chains.get(key):
            key = random.choice(chains.keys())
            continue # continue on to the next iteration
            # why wasn't this continue here already...did someone delete it? -__-

        # if key has an end punctuation, break out of the while loop and return the completed markov string
        if key in end_keys:
            break
            
        new_word = random.choice(chains[key])
        markov_string += new_word + ' '
        # print i, markov_string
        # print ''

        # create a new key
        new_key_list = list(key[1:])
        new_key_list.append(new_word)
        key = tuple(new_key_list)

    return markov_string

# takes in sentence and checks for end punctuation
def sentence_checker(sentence):
    # index will be -2 since we are adding a space to the end of each word added to the markov string
    if sentence[-2] in ['!', '?', '.', '~'] and len(sentence) < 140:
        return True
    else:
        return False

def main():
    # allows unspecified number of arguments
    args = sys.argv
    # Ensure user inputs at least one text file
    # isValid = True
    # Don't need this isValid boolean! 

    if len(args) < 2:
        print "Please provide at least one .txt file."
        # isValid = False
        return
        # return will break out of the main function

    # Check if args exists
    for f in args:
        if not exists(f):
            print "%r does not exist." % f
            # isValid = False
            return

    # if isValid:

    # get raw input from user for n, to be passed into make_text
    # n = int(raw_input("How many n's in your grams? > "))
    n = 2

    # get raw input for char length of final markov string
    # x = int(raw_input("What is the maximum number of characters in your text? > "))
    x = 140

    input_text = ""
    for i in range(1,len(args)):
        f = open(args[i])
        for j in xrange(200):
            input_text += f.readline()

    chain_dict = make_chains(input_text, n) # dictionary
    cap_keys = capital_start(chain_dict) # list of keys
    end_keys = end_punct(chain_dict) # list of keys

    random_text = 'initial placeholder text'
    isTweet = False

    while not isTweet:
        # check if sentence satisfies our specifications
        while not sentence_checker(random_text):
            # print 'checking sentence %r' % random_text
            random_text = make_text(chain_dict, cap_keys, end_keys, n, x)
        print random_text

        # ask user if we should tweet the generated markov chain
        should_we_tweet = raw_input('Would you like to tweet this message(Y/N)? ')

        # Tweet if user says yes. If no, reset random_text to generate another markov chain. 
        if should_we_tweet == 'Y' or should_we_tweet == 'y':
            tweet(random_text)
            isTweet = True
        else:
            random_text = 'initial placeholder text'

if __name__ == "__main__":
    main()
