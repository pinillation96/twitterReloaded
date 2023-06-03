# twitter_reloaded.py
from domain.service.tweet_factory import TweetFactory
from domain.service.comment_decorator import CommentDecorator

class TwitterReloaded:
    def __init__(self, tweet_factory, event_logger):
        self.tweet_factory = tweet_factory
        self.event_logger = event_logger
        self.tweets = {}
        self.next_id = 1

    def create_tweet(self, user, content):
        tweet, event = self.tweet_factory.create_tweet(user, content)
        # Assign an ID to the tweet and increment the next ID
        tweet.id = self.next_id
        self.next_id += 1
        # Store the tweet by its ID
        self.tweets[tweet.id] = tweet
        # Notify Event Dashboard about this event
        self.event_logger.log_event(event)
        return tweet, event

    def reply_to_tweet(self, user, id, content):
        # Retrieve the tweet by its ID
        tweet = self.get_tweet_by_id(id)
        reply, event = CommentDecorator.add_comment(user, tweet, content)
        # Notify Event Dashboard about this event
        self.event_logger.log_event(event)
        return reply, event
    
    def login(self, user):
        self.event_logger.log_open_app(user)

    def get_recent_tweets(self, n):
        # Sort tweets by timestamp in descending order and get the first 'n'
        sorted_tweets = sorted(self.tweets.values(), key=lambda tweet: tweet.timestamp, reverse=True)
        return sorted_tweets[:n]

    def get_tweet_by_id(self, id):
        return self.tweets.get(id)