from django.contrib import admin
from . import models

admin.site.register(models.Feed)
admin.site.register(models.FeedEntry)
admin.site.register(models.ChosenFeed)
