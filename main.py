from tweepy import OAuthHandler, Stream, StreamListener, API, models
from dateutil.parser import parse
import json

#Load credentials (local testing)
with open('credentials.json') as json_file:
    config = json.load(json_file)
    CONSUMER_KEY    = config["CONSUMER_KEY"]
    CONSUMER_SECRET = config["CONSUMER_SECRET"]
    ACCESS_TOKEN    = config["ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET = config["ACCESS_TOKEN_SECRET"]

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

    return tweet_date,tweet_user,tweet_text

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


hashtag_to_track = ['bolsonaro','lula']

if __name__ == "__main__":
    try:
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = API(auth)
        api_owner = api.me()
    except:
        print("Error: Unable to authenticate")

    try:
        myStream = Stream(auth=api.auth, listener=Listener())
        myStream.filter(track=hashtag_to_track)
    except Exception as e:
        myStream.disconnect()
        print(str(e))
        print.exit("Twitter stream disconnected")
