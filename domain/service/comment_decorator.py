# comment_decorator.py
from datetime import datetime
from domain.model.event import Event
from domain.model.tweet import Tweet

class CommentDecorator:
    @staticmethod
    def add_comment(user, tweet, content):
        reply = Tweet(content, user)
        tweet.add_reply(reply)
        event = Event('reply tweet', user, datetime.now())
        return reply, event
