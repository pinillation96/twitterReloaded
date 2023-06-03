import unittest
from datetime import datetime
from domain.model.user import User
from domain.model.tweet import Tweet
from domain.model.event import Event
from domain.service.tweet_factory import TweetFactory
from domain.service.comment_decorator import CommentDecorator
from application.twitter_reloaded import TwitterReloaded
from reports.event_dashboard import EventDashboard

class TestTwitterReloaded(unittest.TestCase):

    def setUp(self):
        self.alice = User("Alice")
        self.bob = User("Bob")
        self.tweet_content = "Hello, world!"
        self.reply_content = "Hi Alice!"

    def test_tweet_creation(self):
        tweet, event = TwitterReloaded.create_tweet(self.alice, self.tweet_content)
        self.assertIsInstance(tweet, Tweet)
        self.assertEqual(tweet.content, self.tweet_content)
        self.assertEqual(tweet.user, self.alice)
        self.assertIsInstance(event, Event)
        self.assertEqual(event.action_type, 'create tweet')
        self.assertEqual(event.user, self.alice)

    def test_reply_to_tweet(self):
        tweet, _ = TwitterReloaded.create_tweet(self.alice, self.tweet_content)
        reply, event = TwitterReloaded.reply_to_tweet(self.bob, tweet, self.reply_content)
        self.assertIsInstance(reply, Tweet)
        self.assertEqual(reply.content, self.reply_content)
        self.assertEqual(reply.user, self.bob)
        self.assertIsInstance(event, Event)
        self.assertEqual(event.action_type, 'reply tweet')
        self.assertEqual(event.user, self.bob)

    def test_event_dashboard(self):
        event_dashboard = EventDashboard()
        tweet, event1 = TwitterReloaded.create_tweet(self.alice, self.tweet_content)
        event_dashboard.update(event1)
        reply, event2 = TwitterReloaded.reply_to_tweet(self.bob, tweet, self.reply_content)
        event_dashboard.update(event2)
        self.assertEqual(event_dashboard.get_most_active_user(), self.bob.username)
        self.assertEqual(event_dashboard.get_user_activity(), {self.alice.username: 1, self.bob.username: 1})

if __name__ == '__main__':
    unittest.main()
