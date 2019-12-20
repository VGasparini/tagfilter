from config import *
from stream import *

# Setup keywords or hashtags to track


class Extractor():
    def __init__(self, hashtag_to_track):
        credentials = Credentials().authenticate()
        try:
            self.api = API(credentials)
            self.api_owner = api.me()
        except:
            print("Error: Unable to authenticate")

        self.hashtag_to_track = hashtag_to_track
        self.streams = list()

    def run(self):
        try:
            for tag in self.hashtag_to_track:
                listener = Listener()
                # Setting limit to better data visualization
                listener.set_limit(10)
                myStream = Stream(auth=self.api.auth, listener=listener)
                myStream.filter(track=[tag], is_async=True)
                self.streams.append(myStream)
        except Exception as e:
            myStream.disconnect()
            print(str(e))
            print.exit("Twitter stream disconnected")
