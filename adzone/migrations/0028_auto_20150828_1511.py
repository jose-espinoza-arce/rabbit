# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adzone', '0027_auto_20150828_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adimpression',
            name='ad',
            field=models.ForeignKey(related_name='impressions', to='adzone.AdBase'),
        ),
    ]
