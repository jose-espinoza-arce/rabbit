# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_forms', '0004_formmodel_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formmodel',
            name='header',
            field=models.TextField(verbose_name='Header', blank=True),
        ),
    ]
