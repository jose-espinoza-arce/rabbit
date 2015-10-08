# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0030_contentlistimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adcategory',
            options={'verbose_name': 'Ad category', 'verbose_name_plural': 'Ad categories'},
        ),
        migrations.AlterModelOptions(
            name='bannerad',
            options={'verbose_name': 'Banner Ad', 'verbose_name_plural': 'Banner Ads'},
        ),
        migrations.AlterModelOptions(
            name='videoad',
            options={'verbose_name': 'Video Ad', 'verbose_name_plural': 'Video Ads'},
        ),
    ]
