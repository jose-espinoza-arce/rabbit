# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import analytics.models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0004_auto_20151012_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkedinstat',
            name='image',
            field=models.ImageField(upload_to=analytics.models.upload_path_handler, verbose_name='Linkedin Image', blank=True),
        ),
        migrations.AddField(
            model_name='linkedinstat',
            name='lnkpostid',
            field=models.CharField(default=' ', max_length=255, verbose_name='Post ID'),
            preserve_default=False,
        ),
    ]
