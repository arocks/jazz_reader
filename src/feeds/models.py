from django.db import models
from django.conf import settings


class Feed(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    feed_url = models.URLField()

    def __str__(self):
        return self.name if self.name else "<Untitled>"


class FeedEntry(models.Model):
    feed = models.ForeignKey(Feed)
    title = models.CharField(max_length=256)
    guid = models.CharField(max_length=256, unique=True)  # Check the length
    url = models.URLField()
    desc = models.CharField(max_length=1000, null=True, blank=True)
    created = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]


class ChosenFeed(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    feed = models.ForeignKey(Feed)

    def __str__(self):
        return "{} <-> {}".format(self.user.name, self.feed.name)

    class Meta:
        ordering = ["user"]


def add_feed(url, name=""):
    old_feeds = Feed.objects.filter(feed_url=url)
    if old_feeds.exists():
        return old_feeds[0]
    else:
        return Feed.objects.create(name=name, feed_url=url)
