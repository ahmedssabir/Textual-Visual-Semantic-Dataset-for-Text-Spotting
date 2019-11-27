#! /usr/bin/python2
# -*- coding: utf-8 -

#  text file should be like this:
# word1 visual (in each line )
#text file formate (pairs) 
'''
woman holding  
pink umbrella 
women umbrella 
pink holding
woman holding   
'''
#output  
'''
(('woman', 'holding'), ':', 2)
(('holding', 'woman'), ':', 1)
(('pink', 'holding'), ':', 1)
(('women', 'umbrella'), ':', 1)
(('pink', 'umbrella'), ':', 1)
(('umbrella', 'women'), ':', 1)
(('holding', 'pink'), ':', 1)
(('umbrella', 'pink'), ':', 1)
'''


import string
import sys
   
# we call the pairs (text-visual) --> bigrams (acually is not bigrams)
with open('text.txt', 'r') as f:
     filecontents = f.read()

# count bigrams
bigrams = {}
words_punct = filecontents.split()
words = [ w.strip(string.punctuation).lower() for w in words_punct ]

# add special START, END tokens (# you can remove this)
#words = ["START"] + words + ["END"]

for index, word in enumerate(words):
    if index < len(words) - 1:
        w1 = words[index]
        w2 = words[index + 1]
        bigram = (w1, w2)
        if bigram in bigrams:
            bigrams[ bigram ] = bigrams[ bigram ] + 1
        else:
            bigrams[ bigram ] = 1

sorted_bigrams = sorted(bigrams.items(), key = lambda pair:pair[1], reverse = True)

for bigram, count in sorted_bigrams:
     print(bigram, ":", count)
 


