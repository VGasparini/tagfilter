class User:
    def __init__(self, author):
        self.name     = author.name
        self.username = author.screen_name
        self.user_url = author.url

    def get_name(self):
        return self.name
    def get_username(self):
        return self.username
    def get_user_url(self):
        return self.user_url
    
    def __str__(self):
        return '@'+self.username