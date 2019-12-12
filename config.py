from tweepy import OAuthHandler
import os

class Credentials:
    def __init__(self):
        self.CONSUMER_KEY        = os.environ["CONSUMER_KEY"]
        self.CONSUMER_SECRET     = os.environ["CONSUMER_SECRET"]
        self.ACCESS_TOKEN        = os.environ["ACCESS_TOKEN"]
        self.ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]

    def set_credentials(self, **args):
        self.CONSUMER_KEY        = args["CONSUMER_KEY"]
        self.CONSUMER_SECRET     = args["CONSUMER_SECRET"]
        self.ACCESS_TOKEN        = args["ACCESS_TOKEN"]
        self.ACCESS_TOKEN_SECRET = args["ACCESS_TOKEN_SECRET"]
    
    def authenticate(self):
        auth = OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
        return auth
