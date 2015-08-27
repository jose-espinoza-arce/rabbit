# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adzone', '0024_downloadlink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='downloadlink',
            name='filepath',
        ),
    ]
