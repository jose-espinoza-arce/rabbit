# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0010_auto_20151015_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleoportunity',
            name='form_data',
            field=models.OneToOneField(null=True, blank=True, to='dynamic_forms.FormModelData'),
        ),
        migrations.AlterField(
            model_name='saleoportunity',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Client Name'),
        ),
    ]
