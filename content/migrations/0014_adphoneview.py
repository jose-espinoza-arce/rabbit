# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_videoad'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdPhoneView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('view_date', models.DateTimeField(auto_now_add=True, verbose_name='When')),
                ('source_ip', models.GenericIPAddressField(null=True, verbose_name='Who', blank=True)),
                ('ad', models.ForeignKey(to='content.AdBase')),
            ],
            options={
                'verbose_name': 'Ad Phone View',
                'verbose_name_plural': 'Ad Phone Views',
            },
        ),
    ]
