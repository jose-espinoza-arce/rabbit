# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdashboardmodule',
            name='lang',
            field=models.CharField(default='es', max_length=255, verbose_name='Language'),
            preserve_default=False,
        ),
    ]
