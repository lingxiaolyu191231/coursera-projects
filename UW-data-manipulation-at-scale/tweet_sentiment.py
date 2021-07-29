import sys
import json
import ast

def hw():
    print('Hello, world!')

def lines(fp):
    print(str(len(fp.readlines())))

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
    count = 0
    # Read in tweets and store in list: tweets_data
    for line in tweet_file:
        line = line.replace("b'","").replace("'",'').replace('\\\\"','').replace("\\","")
        line = json.loads(line)
        

        if 'text' in line:
            tweet_mes = line['text'].split(' ')
            sent = sum(scores[j] for j in tweet_mes if j in scores.keys())
        else:
            sent = 0
        
        count += 1
        print(sent)


if __name__ == '__main__':
    main()
