# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adzone', '0005_adbase_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adbase',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Slug'),
        ),
    ]
