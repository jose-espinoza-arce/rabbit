# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0005_auto_20151012_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleAnalytics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visitors', models.PositiveIntegerField(verbose_name='Visitors')),
                ('users', models.PositiveIntegerField(verbose_name='Users')),
                ('averagetime', models.PositiveIntegerField(verbose_name='Average time(mins)')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('register', models.OneToOneField(to='analytics.StatRegister')),
            ],
        ),
        migrations.CreateModel(
            name='GooglePlusStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gpidpost', models.CharField(max_length=255, verbose_name='Post ID')),
                ('reached', models.PositiveIntegerField(verbose_name='Gplus scope')),
                ('pluses', models.PositiveIntegerField(verbose_name='Likes')),
                ('comments', models.PositiveIntegerField(verbose_name='Comments')),
                ('impressions', models.PositiveIntegerField(verbose_name='Advert Impressions')),
                ('shares', models.PositiveIntegerField(verbose_name='Shares')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('register', models.OneToOneField(to='analytics.StatRegister')),
            ],
        ),
        migrations.CreateModel(
            name='VideoStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plays', models.PositiveIntegerField(verbose_name='Times played')),
                ('register', models.OneToOneField(to='analytics.StatRegister')),
            ],
        ),
        migrations.AddField(
            model_name='googleadwordsstat',
            name='adsgroupid',
            field=models.CharField(default=' ', max_length=255, verbose_name='Ad Group ID'),
            preserve_default=False,
        ),
    ]
