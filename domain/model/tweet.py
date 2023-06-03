# tweet.py
from datetime import datetime

class Tweet:
    def __init__(self, content, user, timestamp):
        self.content = content
        self.user = user
        self.replies = []
        self.timestamp = timestamp
        self.id = None

    def add_reply(self, reply):
        self.replies.append(reply)