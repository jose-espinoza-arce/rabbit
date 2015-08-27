# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adzone', '0023_adbase_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=255, verbose_name='Key')),
                ('filepath', models.FilePathField(verbose_name='Link Path')),
                ('since', models.DateTimeField(auto_now_add=True, verbose_name='Since')),
                ('url', models.URLField(verbose_name='Url Path')),
                ('ad', models.ForeignKey(related_name='links', to='adzone.AdBase')),
            ],
        ),
    ]
