from tweet import *
from app import *

from tweepy import Stream, StreamListener, API, models

# A listener handles tweets that are received from the stream.
class Listener(StreamListener):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.limit = 10

    def set_limit(self,limit):
        self.limit = limit

    def on_disconnect(self, notice):
        print(notice)

    def on_connect(self):
        print("Stream API Connected")

    def on_status(self, status):
        add_tweet(Tweet(status))

        # Controlling number o tweets to get
        if self.counter < self.limit:
            self.counter += 1
            return True
        else:
            return False

    def on_error(self, status):
        print(status)
