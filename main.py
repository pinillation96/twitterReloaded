""" from domain.model.user import User
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
    main() """
from application.twitter_reloaded import TwitterReloaded
from domain.service.tweet_factory import TweetFactory
from domain.model.user import User
from infrastructure.event_logger import EventLogger
from reports.event_dashboard import EventDashboard

def main():
    print("Welcome to Twitter Reloaded!")
    username = input("Please enter your username to login: ")

    user = User(username)
    twitter_reloaded = TwitterReloaded(TweetFactory(), EventLogger())
    twitter_reloaded.login(user)

    while True:
        print("\nMenu:")
        print("1. Create a tweet")
        print("2. Reply to a tweet")
        print("3. Show dashboard")
        print("4. Show event reports")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            content = input("Enter your tweet (300 characters max): ")
            twitter_reloaded.create_tweet(user, content[:300])
        elif choice == "2":
            tweet_id = input("Enter the ID of the tweet you want to reply to: ")
            tweet = twitter_reloaded.get_tweet_by_id(tweet_id)
            if tweet is not None:
                content = input("Enter your reply (300 characters max): ")
                twitter_reloaded.reply_to_tweet(user, tweet, content[:300])
            else:
                print("Invalid tweet ID. Please try again.")
        elif choice == "3":
            tweets = twitter_reloaded.get_recent_tweets(10)
            for tweet in tweets:
                print(f"{tweet.author.name}: {tweet.content}")
                for reply in tweet.replies:
                    print(f"\t{reply.author.name}: {reply.content}")
        elif choice == "4":
            dashboard = EventDashboard(twitter_reloaded.event_logger)
            print("Most active user today:", dashboard.get_most_active_user().name)
            print("Most commented tweet today:", dashboard.get_most_commented_tweet().content)
            print("Number of users who opened the app today:", dashboard.get_open_app_users())
        elif choice == "5":
            print("Thank you for using Twitter Reloaded!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
