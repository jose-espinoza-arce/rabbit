# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0015_adbase_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerad',
            name='content_mobile',
            field=models.ImageField(default=b'', upload_to=b'adzone/bannerads/mobile', verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='videoad',
            name='content',
            field=models.URLField(verbose_name='Url'),
        ),
    ]
