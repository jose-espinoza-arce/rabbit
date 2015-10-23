# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0008_auto_20151013_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statregister',
            name='ad',
            field=models.OneToOneField(related_name='stats_register', to='content.AdBase'),
        ),
    ]
