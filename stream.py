from tweepy import Stream, StreamListener, API, models
import json

# Utility to extract information from tweet
def format_tweet(data: models.Status) -> str:
    tweet_date = '['+str(data.created_at.time())+']'
    tweet_user = '@'+data.user.screen_name+':'

    # Checking if tweet is a retweet. If true, try to get full_text (length up to 240 char)
    if hasattr(data, "retweeted_status"):
        try:
            text = data.retweeted_status.extended_tweet["full_text"]
        except AttributeError:
            text = data.retweeted_status.text
    else:
        try:
            text = data.extended_tweet["full_text"]
        except AttributeError:
            text = data.text

    tweet_text = '"'+text+'"'

    return tweet_date, tweet_user, tweet_text

# A listener handles tweets that are received from the stream.
class Listener(StreamListener):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.limit = 10

    def on_disconnect(self, notice):
        print(notice)

    def on_connect(self):
        print("Stream API Connected")

    def on_status(self, status):
        print(*format_tweet(status))

        # Controlling number o tweets to get
        if self.counter < self.limit:
            self.counter += 1
            return True
        else:
            return False

    def on_error(self, status):
        print(status)
