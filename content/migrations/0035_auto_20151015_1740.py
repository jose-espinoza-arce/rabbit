# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0034_auto_20151015_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adbase',
            name='actionform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Call to action', to='dynamic_forms.FormModel', null=True),
        ),
    ]
