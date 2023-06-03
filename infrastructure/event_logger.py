# event_logger.py
class EventLogger:
    @staticmethod
    def log_event(event):
        print(f'Logged event: {event.action_type} by user: {event.user.username} at {event.timestamp}')
    def log_open_app(self, user):
        self.events.append(Event(user, "open application"))
