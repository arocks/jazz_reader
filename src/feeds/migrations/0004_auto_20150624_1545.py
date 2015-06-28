# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0003_auto_20150617_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedentry',
            name='created',
            field=models.DateTimeField(),
        ),
    ]
