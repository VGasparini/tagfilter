from server import App
from model import Extractor
from time import sleep

# Controller layer

tweets = list()
tags = set()


def add_tweet(tweet):
    global tweets

    tweets.append(tweet)


def update(extractor):
    global tweets

    for stream in extractor.streams:
        for tweet in stream.listener.tweets:
            add_tweet(tweet[1])


app = App(tweets, tags)
app.run()
sleep(3)
ex = Extractor(tags)
ex.run()
update(ex)
app.run()
sleep(3)
