# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_forms', '0003_auto_20151026_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='formmodel',
            name='header',
            field=models.TextField(max_length=255, verbose_name='Header', blank=True),
        ),
    ]
