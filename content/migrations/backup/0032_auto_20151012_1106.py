# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0031_auto_20151006_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerad',
            name='content',
            field=models.ImageField(upload_to='content/bannerads/', verbose_name='Banner'),
        ),
        migrations.AlterField(
            model_name='bannerad',
            name='content_mobile',
            field=models.ImageField(default='', upload_to='content/bannerads/mobile', verbose_name='Mobile Banner', blank=True),
        ),
        migrations.AlterField(
            model_name='videoad',
            name='content',
            field=models.ImageField(default='', help_text='This image will be used in the list views.', verbose_name='Image', upload_to='content/videoads/'),
        ),
        migrations.AlterField(
            model_name='videoad',
            name='content_mobile',
            field=models.ImageField(default='', upload_to='content/videoads/mobile', blank=True, help_text='This image will be used in the list views for mobiles.', verbose_name='Mobile Image'),
        ),
        migrations.AlterField(
            model_name='videoad',
            name='video_url',
            field=models.URLField(verbose_name='Video'),
        ),
    ]
