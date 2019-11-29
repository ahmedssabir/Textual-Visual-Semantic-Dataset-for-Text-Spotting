#!/bin/bash
#python2.7

#
# pip install gensim

# https://github.com/stanfordnlp/GloVe
#840B tokens, 2.2M vocab, cased, 300d vectors, 2.03 GB download)


import gensim
from gensim.models import Word2Vec

model = Word2Vec.load('word2vec_model2_glov_840B')


file1 = []

file2 = []


with open('object1.txt','rU') as f:     
    for line in f:
   	
       file1.append(line.rstrip())


with open('object2','rU') as f1:    
    
    for line1 in f1: 
       file2.append(line1.rstrip())
     

resutl=[]

f=open('sim-score.txt', "w")




for i in range(len(file1)):
	temp =[]

	try :
	    w = model.similarity(file1[i],file2[i])
	except KeyError : 
	    print('out_of_dict')
	    w = 0  #OVV to 0 

	print "1", file1
	print "2", file2
	temp.append(w)
	result= file1[i]+','+file2[i]+','+str(w)
	#result = file1[i]+',',+file2[i]+','+(w)
	f.write(result)
	f.write('\n')
	print w
f.close()
