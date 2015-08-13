# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adzone', '0006_auto_20150812_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='adbase',
            name='descritption',
            field=models.TextField(default='descricpcion', verbose_name='Description'),
            preserve_default=False,
        ),
    ]
