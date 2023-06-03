# reply.py
from datetime import datetime

class Reply:
    def __init__(self, content, user):
        self.content = content
        self.user = user
        self.timestamp = datetime.now()