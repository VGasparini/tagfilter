'''
Here goes front-end application
'''

tweets = list()

def add_tweet(tweet):
    global tweets
    tweets.append(tweet)
    print(tweet,end='\n\n')

