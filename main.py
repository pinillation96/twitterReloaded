from domain.model.user import User
from application.twitter_reloaded import TwitterReloaded
from infrastructure.event_logger import EventLogger
from reports.event_dashboard import EventDashboard

def main():
    # Instantiate the Event Dashboard
    event_dashboard = EventDashboard()
    
    # Create users
    alice = User("Alice")
    bob = User("Bob")

    # Alice creates a tweet
    tweet, event = TwitterReloaded.create_tweet(alice, "Hello, world!")
    event_dashboard.update(event)
    EventLogger.log_event(event)

    # Bob replies to Alice's tweet
    reply, event = TwitterReloaded.reply_to_tweet(bob, tweet, "Hi Alice!")
    event_dashboard.update(event)
    EventLogger.log_event(event)
    
    # Alice replies to Bob's reply
    second_reply, event = TwitterReloaded.reply_to_tweet(alice, reply, "How are you doing, Bob?")
    event_dashboard.update(event)
    EventLogger.log_event(event)

    # Check reports
    print("Most active user:", event_dashboard.get_most_active_user())
    print("User activity:", event_dashboard.get_user_activity())

if __name__ == "__main__":
    main()
