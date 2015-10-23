# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_forms', '0015_auto_20151012_1106'),
        ('analytics', '0009_auto_20151014_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleoportunity',
            name='form_data',
            field=models.OneToOneField(default=1, blank=True, to='dynamic_forms.FormModelData'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='googleplusstat',
            name='pluses',
            field=models.PositiveIntegerField(verbose_name='Pluses(+1)'),
        ),
        migrations.AlterField(
            model_name='saleoportunity',
            name='ad',
            field=models.ForeignKey(related_name='sales_oportunities', to='content.AdBase'),
        ),
    ]
