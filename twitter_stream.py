from config import *
from stream import *


class Extractor():
    '''
    This class creates the data listener based on a list of tags to filter
    Each listener stores a list of tweets 
    '''

    def __init__(self, hashtag_to_track):
        self.credentials = Credentials().authenticate()
        try:
            self.api = API(self.credentials)
            self.api_owner = api.me()
        except:
            print("Error: Unable to authenticate")

        self.hashtag_to_track = hashtag_to_track
        self.streams = list()

    def run(self):
        try:
            for tag in self.hashtag_to_track:
                listener = Listener()
                # Setting limit to better network usage
                listener.set_limit(3)
                myStream = Stream(auth=self.api.auth, listener=listener)
                myStream.filter(track=[tag], is_async=True)
                self.streams.append(myStream)
        except Exception as e:
            myStream.disconnect()
            print(str(e))
            print.exit("Twitter stream disconnected")
