# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0006_auto_20151012_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statregister',
            name='ad',
            field=models.OneToOneField(to='content.AdBase'),
        ),
    ]
