# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adzone', '0025_remove_downloadlink_filepath'),
    ]

    operations = [
        migrations.AddField(
            model_name='downloadlink',
            name='filepath',
            field=models.FilePathField(default='/', verbose_name='Link Path'),
            preserve_default=False,
        ),
    ]
