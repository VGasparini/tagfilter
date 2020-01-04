import os
from time import sleep
from stdout import log

from flask import Flask, render_template, request, redirect
from twitter_stream import Extractor

# Flask main file. It generate html page and read input data


# Global vars
tweets = list()
ids = set()
tags = set()
extractors = list()
limit = 5


def add_tweet(tweet):
    '''
    Append to tweets list a tuple. Each tuple contains tags information and tweet information
    The tweet ID is added to an IDs set to prevent duplicated tweets
    '''
    global tweets

    tweets.append((tweet[1], tweet[0]))
    ids.add(tweet[1].get_id())


def update(extractors):
    '''
    Iterate above extractors list updating tweets extracted for each
    '''
    global tweets

    for extractor in extractors:
        log("Retrieving data for tag:", str(extractor.hashtag_to_track))
        extractor.run()
        sleep(1)
        for stream in extractor.streams:
            for tweet in stream.listener.tweets:
                if not tweet[1].get_id() in ids:
                    add_tweet((*extractor.hashtag_to_track, tweet[1]))

    tweets.sort(reverse=True)


class App():
    def __init__(self):
        self.app = Flask(__name__)

        @self.app.route("/", methods=['GET', 'POST'])
        def index():

            if request.method == 'POST':
                # Deal with diferrent buttons pressed

                if 'tag_input' in request.form.keys():
                    # Add new tag from input field
                    data = list(request.form['tag_input'].replace(
                        ' ', '').split(';'))
                    for tag in data:
                        tags.add(tag)
                        ex = Extractor([tag])
                        extractors.append(ex)

                elif 'tag_button' in request.form.keys():
                    # Removes tag button when is pressed
                    data = request.form['tag_button']
                    tags.remove(data)

                    # Remove tweets from that tag
                    to_delete = list()
                    for i in range(len(tweets)):
                        if tweets[i][1] == data:
                            to_delete.append(i)
                    for i in to_delete[::-1]:
                        tweets.pop(i)

                    # Destroys that tag stream
                    to_delete = list()
                    for i in range(len(extractors)):
                        if data in extractors[i].hashtag_to_track:
                            for stream in extractors[i].streams:
                                log("Closing", data, "stream")
                                stream.disconnect()
                            to_delete.append(i)
                    for i in to_delete[::-1]:
                        extractors.pop(i)
                else:
                    return redirect(request.url)

            sleep(1)
            # Controlling feed showing
            if len(extractors):
                while(len(tweets) >= limit):
                    tweets.pop(0)
                update(extractors)

            return render_template("index.html", tweets=tweets, tags=tags)

    def run(self):
        port = int(os.environ.get('PORT', 5000))
        self.app.run(host='0.0.0.0', port=port)


app = App()
if __name__ == '__main__':
    app.run()
