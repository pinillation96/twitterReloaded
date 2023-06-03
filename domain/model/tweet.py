# tweet.py
class Tweet:
    def __init__(self, content, user):
        self.content = content
        self.user = user
        self.replies = []

    def add_reply(self, reply):
        self.replies.append(reply)