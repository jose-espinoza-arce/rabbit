# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('adzone', '0011_advertiser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertiser',
            name='phone_number',
            field=models.CharField(default=b'', max_length=16, verbose_name='Phone number', blank=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
        ),
    ]
