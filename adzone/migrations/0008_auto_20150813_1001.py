# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adzone', '0007_adbase_descritption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adbase',
            name='descritption',
            field=models.TextField(verbose_name='Description', blank=True),
        ),
    ]
