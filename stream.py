from tweet import *

from tweepy import Stream, StreamListener, API, models

# A listener handles tweets that are received from the stream.


class Listener(StreamListener):
    def __init__(self):
        super().__init__()
        self.ready = False
        self.limit = 3
        self.tweets = list()

    def set_limit(self, limit):
        self.limit = limit

    def on_disconnect(self, notice):
        print(notice)

    def on_connect(self):
        print("Stream API Connected")

    def on_status(self, status):
        self.tweets.append((len(self.tweets), Tweet(status)))

        # Controlling number o tweets to get
        if len(self.tweets) < self.limit:
            return True
        else:
            self.tweets.pop(0)
            return False

    def on_error(self, status):
        print(status)
