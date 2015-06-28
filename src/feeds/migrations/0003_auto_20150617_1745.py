# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0002_auto_20150617_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedentry',
            name='guid',
            field=models.CharField(unique=True, max_length=256, default='ABC'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feed',
            name='feed_url',
            field=models.URLField(unique=True),
        ),
    ]
