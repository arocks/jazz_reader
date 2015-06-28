# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0005_auto_20150624_1649'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favourite_feed',
            field=models.ForeignKey(blank=True, null=True, to='feeds.Feed'),
        ),
    ]
