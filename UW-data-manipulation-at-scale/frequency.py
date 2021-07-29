#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import json
import re

def hw():
    print('Hello, world!')

def lines(fp):
    print(str(len(fp.readlines())))

def func_rttoskzk(P):
    return P


def main():

    with open(sys.argv[1]) as f1:
        tweet_file = f1.readlines()

    terms = []
    new_tweet_sent = []

    # Read in tweets and store in list: tweets_data
    for line in tweet_file:
        line = line.replace("b'","").replace("'",' ').replace('\\\\"',' ').replace("\\"," ")
        line = json.loads(line)
        
        sent = 0
        if 'text' in line:
            tweet_mes = line['text'].split(' ')
            new_tweet_sent.append(line['text'])
            eng = re.findall(r'[a-z|A-Z]+', line['text'])
            terms.extend(eng)
    
    count_all = len(terms)
    terms = list(set(terms))
    term_dict = dict.fromkeys(terms)
    for i in term_dict:
        term_dict[i] = 0
    
    for tweet in new_tweet_sent:

        words = tweet.split(" ")
        for word in words:
            if word in term_dict.keys():
                term_dict[word] += 1

    term_new_dict = {key: round(value/count_all,4) for key, value in term_dict.items()}             
    
    for key, value in term_new_dict.items():
        print(f'{key} {value}')
            

if __name__ == '__main__':
    main()

