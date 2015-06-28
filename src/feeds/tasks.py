import logging
from urllib.request import urlopen
import feedparser
from datetime import datetime
from time import mktime
from feeds import models
from celery import shared_task


def retrieve_page(url):
    response = urlopen(url)
    page = response.read()
    return page


def parse_feed_title(page):
    d = feedparser.parse(page)
    return d['feed']['title']


def parse_feed_entries(page):
    d = feedparser.parse(page)
    return [models.FeedEntry(
        title=e["title"],
        guid=e.get('guid', e['link']),
        url=e['link'],
        desc=e['summary'],
        created=datetime.fromtimestamp(mktime(e['updated_parsed']))
    ) for e in d['entries']]


@shared_task
def fetch_feed(feed_id):
    feed_obj = models.Feed.objects.get(id=feed_id)
    logger = logging.getLogger("project.fetch_feed")
    logger.debug("Fetching feed: {}".format(feed_obj.name))
    page = retrieve_page(feed_obj.feed_url)
    if not feed_obj.name:
        feed_obj.name = parse_feed_title(page)
        feed_obj.save()
    for entry in parse_feed_entries(page):
        if models.FeedEntry.objects.filter(guid=entry.guid).exists():
            continue
        logger.debug("> Inserting feed entry: {}".format(entry.title))
        entry.feed = feed_obj
        entry.save()


@shared_task
def fetch_all_feeds():
    for f in models.Feed.objects.all():
        fetch_feed.delay(f.id)
