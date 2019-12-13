from config import *
from stream import *

# Setup keywords or hashtags to track
hashtag_to_track = ['celular','android','#apple','#ios']

if __name__ == "__main__":
    credentials = Credentials().authenticate()
    try:
        api = API(credentials)
        api_owner = api.me()
    except:
        print("Error: Unable to authenticate")

    try:
        for tag in hashtag_to_track:
            listener = Listener()
            listener.set_limit(2) # Setting limit to better data visualization
            myStream = Stream(auth=api.auth, listener=listener)
            myStream.filter(track=[tag], is_async=True)
    except Exception as e:
        myStream.disconnect()
        print(str(e))
        print.exit("Twitter stream disconnected")
