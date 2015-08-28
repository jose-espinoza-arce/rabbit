# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adzone', '0026_downloadlink_filepath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adimpression',
            name='ad',
            field=models.ForeignKey(related_name='impresions', to='adzone.AdBase'),
        ),
    ]
