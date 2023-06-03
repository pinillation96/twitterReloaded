# event_dashboard.py
from collections import defaultdict
from operator import itemgetter

class EventDashboard:
    def __init__(self):
        self.events = []
        self.user_event_count = defaultdict(int)

    def update(self, event):
        self.events.append(event)
        self.user_event_count[event.user.username] += 1

    def get_most_active_user(self):
        return max(self.user_event_count.items(), key=itemgetter(1))[0]

    def get_most_commented_tweet(self):
        most_commented_tweet = max((tweet for tweet in self.events if tweet.action_type == 'reply tweet'), 
                                   key=lambda tweet: len(tweet.tweet.replies), default=None)
        return most_commented_tweet

    def get_user_activity(self):
        return self.user_event_count
    def get_open_app_users(self):
        return len([event for event in self.events if event.action_type == "open application"])
