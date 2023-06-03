# event_logger.py
class EventLogger:
    @staticmethod
    def log_event(event):
        print(f'Logged event: {event.action_type} by user: {event.user.username} at {event.timestamp}')