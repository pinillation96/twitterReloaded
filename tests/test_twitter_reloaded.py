""" import unittest
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
 """

import unittest
from unittest.mock import Mock, patch
from datetime import datetime
from application.twitter_reloaded import TwitterReloaded
from domain.model.user import User
from domain.service.tweet_factory import TweetFactory
from infrastructure.event_logger import EventLogger




class TwitterReloadedTests(unittest.TestCase):
    def setUp(self):
        self.user = User("TestUser")
        self.tweet_factory = TweetFactory()
        self.event_logger = EventLogger()
        self.twitter_reloaded = TwitterReloaded(self.tweet_factory, self.event_logger)

    @patch('datetime.datetime.now')
    def test_create_tweet(self, datetime_now):
        datetime_now.return_value = datetime(2022, 1, 1)
        tweet, event = self.twitter_reloaded.create_tweet(self.user, "Test content")
        self.assertEqual(tweet.id, 1)
        self.assertEqual(tweet.timestamp, datetime(2022, 1, 1))
        self.assertEqual(tweet.content, "Test content")
        self.assertEqual(tweet.user, self.user)
        self.assertEqual(self.twitter_reloaded.tweets[1], tweet)

    @patch('datetime.datetime.now')
    def test_reply_to_tweet(self, datetime_now):
        datetime_now.return_value = datetime(2022, 1, 1)
        tweet, event = self.twitter_reloaded.create_tweet(self.user, "Test content")
        reply, event = self.twitter_reloaded.reply_to_tweet(self.user, tweet.id, "Test reply")
        self.assertEqual(reply.content, "Test reply")
        self.assertEqual(reply.user, self.user)
        self.assertIn(reply, tweet.replies)

    @patch('datetime.datetime.now')
    def test_get_recent_tweets(self, datetime_now):
        datetime_now.side_effect = [
            datetime(2022, 1, 1),
            datetime(2022, 1, 2),
            datetime(2022, 1, 3)
        ]
        tweet1, event = self.twitter_reloaded.create_tweet(self.user, "Test content 1")
        tweet2, event = self.twitter_reloaded.create_tweet(self.user, "Test content 2")
        tweet3, event = self.twitter_reloaded.create_tweet(self.user, "Test content 3")
        recent_tweets = self.twitter_reloaded.get_recent_tweets(2)
        self.assertEqual([tweet.id for tweet in recent_tweets], [tweet.id for tweet in [tweet3, tweet2]])

# Execute the tests
if __name__ == "__main__":
    unittest.main()