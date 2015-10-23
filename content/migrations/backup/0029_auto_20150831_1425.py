# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0028_auto_20150828_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adbase',
            name='file',
            field=models.FileField(default=b'', upload_to=b'content/uploads/', verbose_name='File', blank=True),
        ),
        migrations.AlterField(
            model_name='bannerad',
            name='content',
            field=models.ImageField(upload_to=b'content/bannerads/', verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='bannerad',
            name='content_mobile',
            field=models.ImageField(default=b'', upload_to=b'content/bannerads/mobile', verbose_name='Mobile Content', blank=True),
        ),
        migrations.AlterField(
            model_name='videoad',
            name='content',
            field=models.ImageField(default=b'', upload_to=b'content/videoads/', verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='videoad',
            name='content_mobile',
            field=models.ImageField(default=b'', upload_to=b'content/videoads/mobile', verbose_name='Mobile Content', blank=True),
        ),
    ]
