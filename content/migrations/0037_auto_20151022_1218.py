# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0036_auto_20151020_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adbase',
            name='since',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='adbase',
            name='stop_showing',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 11, 12, 18, 43, 374766, tzinfo=utc), verbose_name='Stop showing'),
        ),
    ]
