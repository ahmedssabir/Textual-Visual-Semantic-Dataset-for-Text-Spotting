#!/bin/bash
#python2.7

# pip install gensim
# need to install this crawl-300d-2M.vec
#https://fasttext.cc/docs/en/english-vectors.html

import gensim
from gensim.models import Word2Vec

from gensim.models import FastText


embedding_dict = gensim.models.KeyedVectors.load_word2vec_format("crawl-300d-2M.vec", binary=False)
embedding_dict.save_word2vec_format('saved_model_gensim1'+".bin", binary=True)
model = gensim.models.KeyedVectors.load_word2vec_format('saved_model_gensim1'+".bin", binary=True)

file1 = []

file2 = []


with open('object-1.txt','rU') as f:
    for line in f:
   	    #print line.rstrip()
       file1.append(line.rstrip())



with open('object-2.txt','rU') as f1:
    for line1 in f1:
       file2.append(line1.rstrip())
       

resutl=[]
f=open('sim-fast-text.txt', "w") 



for i in range(len(file1)):
	temp =[]

	try :
	    w = model.similarity(file1[i],file2[i])
	except KeyError : 
	    print('out_of_dict')
	    w = 0 

	print "1", file1
	print "2", file2
	temp.append(w)
	result= file1[i]+','+file2[i]+','+str(w)

	f.write(result)
	f.write('\n')
	print w
f.close()
