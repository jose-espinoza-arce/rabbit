# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adzone', '0009_auto_20150813_1015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adbase',
            old_name='descritption',
            new_name='description',
        ),
    ]
