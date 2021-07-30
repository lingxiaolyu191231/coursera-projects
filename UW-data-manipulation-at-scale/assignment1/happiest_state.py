#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import json
import ast
import re

def hw():
    print('Hello, world!')

def lines(fp):
    print(str(len(fp.readlines())))

def main():
    
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
        
    }

    with open(sys.argv[1]) as f:
        sent_file = f.readlines()

    with open(sys.argv[2]) as f1:
        tweet_file = f1.readlines()

    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    # Initialize empty list to store tweets: tweets_data
    state_dict = dict.fromkeys(list(states.values()))
    for i in state_dict:
        state_dict[i] = 0
    # Read in tweets and store in list: tweets_data
    for line in tweet_file:
        line = line.replace("b'","").replace("'",'').replace('\\\\"','').replace("\\","")
        line = json.loads(line)
        if 'user' in line:
            if 'location' in line['user']:
                if line['user']['location'] != None:
                    lc = line['user']['location'].split(",")
                    lc = [i.replace(" ","") for i in lc]
                    usa_state = False
                    for l in lc:
                        if l in states.keys():
                            usa_state = True
                            state_name = states[l]
                        elif l in states.values():
                            usa_state = True
                            state_name = l
                        
                        if usa_state==True:
                            break
                        
                    if usa_state==True:
                        if 'text' in line:
                            tweet_mes = line['text'].split(' ')
                            sent = sum(scores[j] for j in tweet_mes if j in scores.keys())
                        else:
                            sent = 0  
                        
                        state_dict[state_name] += sent    
            
            else:
                continue
        else:
            continue
        
    happiest = max(state_dict, key=state_dict.get)
    return happiest


if __name__ == '__main__':
    main()

