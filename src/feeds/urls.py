from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.AllFeedsView.as_view(), name='all_feeds'),
    url(r'^add/$', views.AddFeedView.as_view(), name='add_feed'),
    url(r'^(?P<feednum>\d+)/$', views.SingleFeedView.as_view(), name='single_feed'),
]
