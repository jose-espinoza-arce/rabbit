# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import analytics.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20151023_1209'),
        ('dynamic_forms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fbpostid', models.CharField(max_length=255, verbose_name='Post ID')),
                ('image', models.ImageField(upload_to=analytics.models.upload_path_handler, verbose_name='Facebook Image', blank=True)),
                ('reached', models.PositiveIntegerField(verbose_name='Reached people')),
                ('likes', models.PositiveIntegerField(verbose_name='Likes')),
                ('comments', models.PositiveIntegerField(verbose_name='Comments')),
                ('shares', models.PositiveIntegerField(verbose_name='Shares')),
                ('clicks', models.PositiveIntegerField(verbose_name='Advert Clicks')),
                ('link_clicks', models.PositiveIntegerField(null=True, verbose_name='Link Clicks', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoogleAdWordsStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('adsgroupid', models.CharField(max_length=255, verbose_name='Ad Group ID')),
                ('clicks', models.PositiveIntegerField(verbose_name='Advert Clicks')),
                ('impressions', models.PositiveIntegerField(verbose_name='Advert Impressions')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoogleAnalytics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visitors', models.PositiveIntegerField(verbose_name='Visitors')),
                ('users', models.PositiveIntegerField(verbose_name='Users')),
                ('averagetime', models.PositiveIntegerField(verbose_name='Average time(mins)')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GooglePlusStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gpidpost', models.CharField(max_length=255, verbose_name='Post ID')),
                ('reached', models.PositiveIntegerField(verbose_name='Gplus scope')),
                ('pluses', models.PositiveIntegerField(verbose_name='Pluses(+1)')),
                ('comments', models.PositiveIntegerField(verbose_name='Comments')),
                ('impressions', models.PositiveIntegerField(verbose_name='Advert Impressions')),
                ('shares', models.PositiveIntegerField(verbose_name='Shares')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LinkedinStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lnkpostid', models.CharField(max_length=255, verbose_name='Post ID')),
                ('image', models.ImageField(upload_to=analytics.models.upload_path_handler, verbose_name='Linkedin Image', blank=True)),
                ('reached', models.PositiveIntegerField(verbose_name='Linkedin Members')),
                ('clicks', models.PositiveIntegerField(verbose_name='Advert Clicks')),
                ('impressions', models.PositiveIntegerField(verbose_name='Advert Impressions')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SaleOportunity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Client Name')),
                ('phone_number', models.CharField(default=b'', max_length=16, verbose_name='Phone number', blank=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b'Enter a valid phone number.')])),
                ('email', models.EmailField(max_length=254, verbose_name=b'Correo')),
                ('source', models.PositiveSmallIntegerField(verbose_name='Source', choices=[(1, b'No especificado'), (2, b'Roofmedia'), (3, b'Facebook'), (4, b'GoogleAdWords'), (5, b'Linkedin')])),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ad', models.ForeignKey(related_name='sales_oportunities', to='content.AdBase')),
                ('form_data', models.OneToOneField(null=True, blank=True, to='dynamic_forms.FormModelData')),
            ],
            options={
                'ordering': ('-created_at',),
                'verbose_name': 'Oportunidad de venta',
                'verbose_name_plural': 'Oportunidades de venta',
            },
        ),
        migrations.CreateModel(
            name='StatRegister',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ad', models.OneToOneField(related_name='stats_register', to='content.AdBase')),
            ],
            options={
                'ordering': ('created_at',),
                'verbose_name': 'Register',
                'verbose_name_plural': 'Registry',
            },
        ),
        migrations.CreateModel(
            name='VideoStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plays', models.PositiveIntegerField(verbose_name='Times played')),
                ('register', models.OneToOneField(related_name='video_stats', to='analytics.StatRegister')),
            ],
        ),
        migrations.AddField(
            model_name='linkedinstat',
            name='register',
            field=models.OneToOneField(related_name='linkedin_stats', to='analytics.StatRegister'),
        ),
        migrations.AddField(
            model_name='googleplusstat',
            name='register',
            field=models.OneToOneField(related_name='googleplus_stats', to='analytics.StatRegister'),
        ),
        migrations.AddField(
            model_name='googleanalytics',
            name='register',
            field=models.OneToOneField(related_name='googlean_stats', to='analytics.StatRegister'),
        ),
        migrations.AddField(
            model_name='googleadwordsstat',
            name='register',
            field=models.OneToOneField(related_name='googleadword_stats', to='analytics.StatRegister'),
        ),
        migrations.AddField(
            model_name='facebookstat',
            name='register',
            field=models.OneToOneField(related_name='facebook_stats', to='analytics.StatRegister'),
        ),
    ]
