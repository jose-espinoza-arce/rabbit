# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_forms', '0015_auto_20151012_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formmodeldata',
            name='form',
            field=models.ForeignKey(related_name='data', to='dynamic_forms.FormModel', null=True),
        ),
    ]
