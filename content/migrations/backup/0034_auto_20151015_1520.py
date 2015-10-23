# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0033_auto_20151014_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adphoneview',
            name='ad',
            field=models.ForeignKey(related_name='phone_views', to='content.AdBase'),
        ),
    ]
