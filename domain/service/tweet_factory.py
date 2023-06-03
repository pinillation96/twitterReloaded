# tweet_factory.py
from datetime import datetime
from domain.model.event import Event
from domain.model.tweet import Tweet

class TweetFactory:
    id_counter = 1  # Class variable to generate unique IDs for tweets

    @staticmethod
    def create_tweet(user, content):
        timestamp = datetime.now()
        tweet = Tweet(content, user, timestamp)
        tweet.id = TweetFactory.id_counter
        TweetFactory.id_counter += 1  # Increment the counter for next ID
        user.add_tweet(tweet)
        event = Event('create tweet', user, datetime.now())
        return tweet, event