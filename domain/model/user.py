# user.py
class User:
    def __init__(self, username):
        self.username = username
        self.tweets = []

    def add_tweet(self, tweet):
        self.tweets.append(tweet)