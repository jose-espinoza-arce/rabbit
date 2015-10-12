# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import analytics.models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_auto_20151006_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='facebookstat',
            name='fbpostid',
            field=models.CharField(default=' ', max_length=255, verbose_name='Post ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='facebookstat',
            name='image',
            field=models.ImageField(upload_to=analytics.models.upload_path_handler, verbose_name='Facebook Image', blank=True),
        ),
        migrations.AlterField(
            model_name='facebookstat',
            name='likes',
            field=models.PositiveIntegerField(verbose_name='Likes'),
        ),
        migrations.AlterField(
            model_name='facebookstat',
            name='link_clicks',
            field=models.PositiveIntegerField(verbose_name='Link Clicks', blank=True),
        ),
    ]
