# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0035_auto_20151015_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adbase',
            name='description',
            field=models.TextField(max_length=450, verbose_name='Description', blank=True),
        ),
    ]
