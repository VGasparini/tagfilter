from config import *
from stream import *

hashtag_to_track = ['bolsonaro', 'lula']

if __name__ == "__main__":
    credentials = Credentials().authenticate()
    try:
        api = API(credentials)
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
