#!/usr/bin/python
# coding: utf-8
import os,re,sys,nltk
from nltk import word_tokenize
from nltk.util import ngrams
from nltk.corpus import stopwords

# determine value of n in the current block of ngrams by parsing the filename

for line in sys.stdin:
    x = re.sub('[^a-zA-Z ]','',line).lower() #filtering special characters
    tokenized_data =[i for i in nltk.word_tokenize(x) if i not in stopwords.words('english')]
    bigram = [" ".join(i) for i in list(ngrams(tokenized_data,2))] 
    for word in bigram:
        print '%s\t%s' % (word, 1)


