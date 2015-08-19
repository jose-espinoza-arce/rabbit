# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adzone', '0017_auto_20150815_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoad',
            name='content',
            field=models.ImageField(default=b'', upload_to=b'adzone/videoads/', verbose_name='Content'),
        ),
    ]
