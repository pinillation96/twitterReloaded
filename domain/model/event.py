# event.py
class Event:
    def __init__(self, action_type, user, timestamp):
        self.action_type = action_type
        self.user = user
        self.timestamp = timestamp