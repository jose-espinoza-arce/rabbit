# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adzone', '0019_videoad_content_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoad',
            name='content_mobile',
            field=models.ImageField(default=b'', upload_to=b'adzone/videoads/mobile', verbose_name='Mobile Content', blank=True),
        ),
    ]
