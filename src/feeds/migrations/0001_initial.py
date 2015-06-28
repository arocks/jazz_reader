# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChosenFeed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('feed_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='FeedEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('url', models.URLField()),
                ('desc', models.CharField(blank=True, max_length=1000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('feed', models.ForeignKey(to='feeds.Feed')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='chosenfeed',
            name='feed',
            field=models.ForeignKey(to='feeds.Feed'),
        ),
        migrations.AddField(
            model_name='chosenfeed',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
