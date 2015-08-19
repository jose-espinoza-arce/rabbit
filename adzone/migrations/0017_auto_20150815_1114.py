# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adzone', '0016_auto_20150815_1114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videoad',
            old_name='content',
            new_name='video_url',
        ),
    ]
