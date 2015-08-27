# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adzone', '0022_auto_20150818_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='adbase',
            name='file',
            field=models.FileField(default=b'', upload_to=b'adzone/uploads/', verbose_name='File', blank=True),
        ),
    ]
