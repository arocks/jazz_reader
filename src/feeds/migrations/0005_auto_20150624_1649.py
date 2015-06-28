# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_auto_20150624_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='feed_url',
            field=models.URLField(),
        ),
    ]
