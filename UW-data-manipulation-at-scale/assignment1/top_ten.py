#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import json
import ast

def hw():
    print('Hello, world!')

def lines(fp):
    print(str(len(fp.readlines())))

def main():

    with open(sys.argv[1]) as f1:
        tweet_file = f1.readlines()

    hashtag = {}
    # Read in tweets and store in list: tweets_data
    for line in tweet_file:
        line = line.replace("b'","").replace("'",'').replace('\\\\"','').replace("\\","")
        line = json.loads(line)
        

        if 'entities' in line:
            if 'hashtags' in line['entities']:
                for htag in line['entities']['hashtags']:
                    if htag['text'] in hashtag.keys():
                        hashtag[htag['text']] += 1
                    else:
                        hashtag[htag['text']] = 1
    
    sorted_hashtag = sorted(hashtag.items(), key=lambda x: x[1], reverse=True)
    for i in sorted_hashtag[:10]:
        print(f'{i[0]} {i[1]}')
    
if __name__ == '__main__':
    main()


# In[ ]:




