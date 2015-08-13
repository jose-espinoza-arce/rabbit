# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adzone', '0008_auto_20150813_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adbase',
            name='descritption',
            field=models.CharField(max_length=450, verbose_name='Description', blank=True),
        ),
    ]
