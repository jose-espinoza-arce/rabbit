# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20150811_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertiser',
            name='email',
            field=models.EmailField(default='cliente@mw.com', max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
    ]
