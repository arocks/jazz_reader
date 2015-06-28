from django.test import TestCase
from feeds import models
from feeds import tasks


class FeedSelectionTestCase(TestCase):

    def test_user_adds_unnamed_feed(self):
        url = "http://example.com"
        models.add_feed(url)
        self.assertTrue(models.Feed.objects.filter(feed_url=url).exists())

    def test_user_adds_existing_feed(self):
        url = "http://example2.com"
        models.add_feed(url, name="URL 1")
        models.add_feed(url, name="URL 2")  # This should not overwrite the old name
        feeds = models.Feed.objects.filter(feed_url=url)
        self.assertEqual(len(feeds), 1)
        self.assertEqual(feeds[0].name, "URL 1")


class AsyncFeedTasks(TestCase):

    def setUp(self):
        self.feed_url = "http://feeds.bbci.co.uk/news/rss.xml?edition=int"
        self.feed = open("feeds/test_feed.xml").read()

    def test_process_feed(self):
        l = tasks.parse_feed_entries(self.feed)
        self.assertEqual(len(l), 68)
