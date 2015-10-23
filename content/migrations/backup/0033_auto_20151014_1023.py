# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0032_auto_20151012_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adclick',
            name='ad',
            field=models.ForeignKey(related_name='clicks', to='content.AdBase'),
        ),
    ]
