# twitter_reloaded.py
from domain.service.tweet_factory import TweetFactory
from domain.service.comment_decorator import CommentDecorator

class TwitterReloaded:
    @staticmethod
    def create_tweet(user, content):
        tweet, event = TweetFactory.create_tweet(user, content)
        # Notify Event Dashboard about this event
        # event_dashboard.update(event)
        return tweet, event

    @staticmethod
    def reply_to_tweet(user, tweet, content):
        reply, event = CommentDecorator.add_comment(user, tweet, content)
        # Notify Event Dashboard about this event
        # event_dashboard.update(event)
        return reply, event
    def login(self, user):
        self.event_logger.log_open_app(user)