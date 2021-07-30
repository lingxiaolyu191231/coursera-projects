# UW Data Manipulation At Scale: Systems and Algorithms

## Folder Architecture

- twitterstream.py
    Export real-time twitter streaming data
- tweet_sentiment.py
    Analyze sentimental scores for each tweet
- term_sentiment.py
    Create new sentimental scores for terms not in pre-defined sentimental file
- frequency.py
    Calculate term frequency for each word in all tweets and return the sorted term by frequency from highest to lowest
- happiest_state.py
    Calculate sentimental scores by state (summing up sentimental scores by states)
- top_ten.py
    Calculate the Top 10 hashtags most frequently appeared in all tweets
    
## Inustruction:
1. First, run twitterstream.py to export streaming tweets into a text file with tweet info in json format \
    $ python twitterstream.py > output.txt (name any file as you prefer)
2. Then run following files as needed.
    - For tweet_sentiment.py \
        $ python tweet_sentiment.py AFINN-111.txt output.txt
    - For term_sentiment.py \
        $ python term_sentiment.py AFINN-111.txt output.txt
    - For frequency.py \
        $ python frequency.py output.txt
    - For happiest_state.py \
        $ python happiest_state.py AFINN-111.txt output.txt
    - For top_ten.py \ 
        $ python top_ten.py output.txt
