# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_auto_20151012_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebookstat',
            name='link_clicks',
            field=models.PositiveIntegerField(null=True, verbose_name='Link Clicks', blank=True),
        ),
    ]
