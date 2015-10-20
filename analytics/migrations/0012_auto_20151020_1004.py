# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0011_auto_20151015_1648'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='saleoportunity',
            options={'ordering': ('-created_at',), 'verbose_name': 'Oportunidad de venta', 'verbose_name_plural': 'Oportunidades de venta'},
        ),
        migrations.AlterField(
            model_name='saleoportunity',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='saleoportunity',
            name='phone_number',
            field=models.CharField(default=b'', max_length=16, verbose_name='Phone number', blank=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b'Enter a valid phone number.')]),
        ),
    ]
