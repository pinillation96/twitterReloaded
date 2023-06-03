# twitter_reloaded.py
from domain.service.tweet_factory import TweetFactory
from domain.service.comment_decorator import CommentDecorator

class TwitterReloaded:
    def __init__(self, tweet_factory, event_logger):
        self.tweet_factory = tweet_factory
        self.event_logger = event_logger

    def create_tweet(self, user, content):
        tweet, event = self.tweet_factory.create_tweet(user, content)
        # Notify Event Dashboard about this event
        # self.event_logger.log_event(event)
        return tweet, event

    def reply_to_tweet(self, user, tweet, content):
        reply, event = CommentDecorator.add_comment(user, tweet, content)
        # Notify Event Dashboard about this event
        # self.event_logger.log_event(event)
        return reply, event
    
    def login(self, user):
        self.event_logger.log_open_app(user)