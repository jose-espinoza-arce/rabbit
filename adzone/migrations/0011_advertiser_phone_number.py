# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adzone', '0010_auto_20150813_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertiser',
            name='phone_number',
            field=models.CharField(default=b'', max_length=16, verbose_name='Phone number', blank=True),
        ),
    ]
