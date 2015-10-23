# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_forms', '0016_auto_20151015_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formmodeldata',
            name='form',
            field=models.ForeignKey(related_name='data', on_delete=django.db.models.deletion.SET_NULL, to='dynamic_forms.FormModel', null=True),
        ),
    ]
