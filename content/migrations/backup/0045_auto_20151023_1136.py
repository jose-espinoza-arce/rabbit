# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import content.models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0044_auto_20151023_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adbase',
            name='stop_showing',
            field=models.DateTimeField(default=content.models.max_datetime, verbose_name='Stop showing'),
        ),
    ]
