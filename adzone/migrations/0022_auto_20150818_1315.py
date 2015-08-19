# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adzone', '0021_auto_20150815_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerad',
            name='content_mobile',
            field=models.ImageField(default=b'', upload_to=b'adzone/bannerads/mobile', verbose_name='Mobile Content', blank=True),
        ),
    ]
