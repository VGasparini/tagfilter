from user import *

class Tweet:
    def __init__(self, data):
        self.date = data.created_at.time()
        self.user = User(data.author)
        self.id = data.id_str
        self.tweet_url = 'twitter.com/{}/status/{}'.format(self.user.get_username(),self.id)
        self.is_quote = data.is_quote_status
        self.hashtags = [tag['text'] for tag in data.entities['hashtags']]

        '''
        If is a quote tweet, creates new 3 attr:
            original_tweet_url contains url to original tweet that is quoted
            original_tweet_user contains an User object about original tweet user
            quote_text wich contains quote text. It tryies to get 240 version.
        '''
        if self.is_quote:
            self.original_tweet_url = data.quoted_status_permalink['url']
            self.original_tweet_user = User(data.quoted_status.author)
            if data.quoted_status.truncated:
                self.quote_text = data.quoted_status.extended_tweet["full_text"]
            else:
                self.quote_text = data.quoted_status.text
        
        if data.truncated:
            self.original_text = data.extended_tweet["full_text"]
        else:
            self.original_text = data.text

    def __str__(self):
        tweet_date = '['+str(self.date)+'] '
        tweet_user = str(self.user)
        tweet_text = ''
        if self.is_quote:
            tweet_text = 'Quote\n"'+self.quote_text+'" '+self.tweet_url+'\nRetuitando @'+self.original_tweet_user.get_username() 
        tweet_text += '"'+self.original_text+'" '+self.tweet_url

        return tweet_date+'\n'+tweet_user+'\n'+tweet_text+'\nTags: '+' '.join(self.hashtags)
