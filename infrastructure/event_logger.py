# event_logger.py
from domain.model.event import Event
from domain.model.user import User
from datetime import datetime

class EventLogger:
    def __init__(self):
        self.events = []

    def log_event(self, event: Event):
        self.events.append(event)
    
    def log_open_app(self, user: User):
        self.events.append(Event("open application", user, datetime.now()))