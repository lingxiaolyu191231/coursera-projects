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
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    with open(sys.argv[1]) as f:
        sent_file = f.readlines()

    with open(sys.argv[2]) as f1:
        tweet_file = f1.readlines()

    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    # Initialize empty list to store tweets: tweets_data
    print(f'Sentimental scores for each tweet')
    tweet_sent = {}

    # Read in tweets and store in list: tweets_data
    for line in tweet_file:
        line = line.replace("b'","").replace("'",' ').replace('\\\\"',' ').replace("\\"," ")
        line = json.loads(line)
        
        sent = 0
        if 'text' in line:
            tweet_mes = line['text'].split(' ')
            sent = sum(scores[j] for j in tweet_mes if j in scores.keys())
            tweet_sent[line['text']] = sent

    terms = []
    new_tweet_sent = {}
    for i in tweet_sent:
        if tweet_sent[i] != 0:
            new_tweet_sent[i] = tweet_sent[i]
            eng = re.findall(r'[a-z|A-Z]+', i)
            terms.extend(eng)

    terms = list(set(terms))
    term_dict = dict.fromkeys(terms)
    for i in term_dict:
        term_dict[i] = {}
    
    for key in new_tweet_sent:
        P, N = 0, 0
        if new_tweet_sent[key] > 0:
            P = 1
        else:
            N = 1

        words = key.split(" ")
        for word in words:
            if word in term_dict:
                if term_dict[word] == {}:
                    term_dict[word]['P'] = 0
                    term_dict[word]['N'] = 0
                else:
                    term_dict[word]['P'] += P
                    term_dict[word]['N'] += N

    term_new_dict = {key: value for key, value\
                  in term_dict.items()\
                  if value != {}}             
    
    for key, value in term_new_dict.items():
        if value['N'] != 0:
            x = int(value['P'])/int(value['N'])
            print(f'{key} {round(x,4)}')
            
            

if __name__ == '__main__':
    main()
