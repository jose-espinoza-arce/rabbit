# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0038_auto_20151022_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adbase',
            name='stop_showing',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 12, 10, 18, 1, 894378, tzinfo=utc), verbose_name='Stop showing'),
        ),
    ]
