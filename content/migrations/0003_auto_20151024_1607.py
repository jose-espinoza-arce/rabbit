# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20151023_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=255, verbose_name='Ubicaci\xf3n')),
            ],
        ),
        migrations.AddField(
            model_name='adbase',
            name='location',
            field=models.ForeignKey(default=1, verbose_name='Ubicaci\xf3n', to='content.Location'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertiser',
            name='location',
            field=models.ForeignKey(default=1, verbose_name='Ubucaci\xf3n', to='content.Location'),
            preserve_default=False,
        ),
    ]
