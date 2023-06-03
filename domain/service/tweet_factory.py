# tweet_factory.py
from datetime import datetime
from domain.model.event import Event
from domain.model.tweet import Tweet

class TweetFactory:
    @staticmethod
    def create_tweet(user, content):
        tweet = Tweet(content, user)
        user.add_tweet(tweet)
        event = Event('create tweet', user, datetime.now())
        return tweet, event
