# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_forms', '0006_auto_20150811_1549'),
        ('adzone', '0002_auto_20150810_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='adbase',
            name='actionform',
            field=models.ForeignKey(default=1, verbose_name='Call to action', to='dynamic_forms.FormModel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adcategory',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
    ]
