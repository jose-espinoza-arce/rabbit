# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adzone', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adcategory',
            old_name='title',
            new_name='name',
        ),
    ]
