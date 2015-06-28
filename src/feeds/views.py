from django.views import generic
from django.shortcuts import redirect
from django.contrib import messages
from . import models
from . import forms
from . import tasks


class ChosenFeedsMixin(object):

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["feeds"] = self.request.user.chosenfeed_set.order_by("-id")
        return kwargs


class FeedTitleMixin(object):

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["feed_title"] = self.get_feed_title()
        return kwargs


class AllFeedsView(FeedTitleMixin, ChosenFeedsMixin, generic.ListView):
    template_name = "feed_two_pane.html"
    context_object_name = "entries"
    paginate_by = 20

    def get_queryset(self):
        return models.FeedEntry.objects.filter(
            feed__chosenfeed__user=self.request.user).order_by("-created")

    def get_feed_title(self):
        return "All Feeds"


class SingleFeedView(AllFeedsView):
    def get_queryset(self):
        feed = models.Feed.objects.get(pk=self.kwargs["feednum"])
        return feed.feedentry_set.order_by("-created")

    def get_feed_title(self):
        feed = models.Feed.objects.get(pk=self.kwargs["feednum"])
        return feed.name


class AddFeedView(ChosenFeedsMixin, generic.CreateView):
    model = models.Feed
    template_name = "add_feed.html"
    form_class = forms.AddFeedForm

    def form_valid(self, form):
        # TODO: Add async task for initial retrieve of the feed
        url = form.cleaned_data["feed_url"]
        if models.Feed.objects.filter(feed_url=url).exists():
            feed_obj = models.Feed.objects.get(feed_url=url)
        else:
            self.object = form.save()
            feed_obj = self.object
        tasks.fetch_feed.delay(feed_obj.id)
        models.ChosenFeed.objects.get_or_create(user=self.request.user, feed=feed_obj)
        messages.success(self.request, "Feed was sucessfully added")
        return redirect("feeds:all_feeds")
