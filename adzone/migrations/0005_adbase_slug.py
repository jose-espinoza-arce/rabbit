# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adzone', '0004_advertiser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='adbase',
            name='slug',
            field=models.SlugField(default='slug', verbose_name='Slug'),
            preserve_default=False,
        ),
    ]
