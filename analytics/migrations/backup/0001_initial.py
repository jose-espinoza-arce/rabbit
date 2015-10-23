# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0031_auto_20151006_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reached', models.PositiveIntegerField(verbose_name='Reached people')),
                ('likes', models.PositiveIntegerField(verbose_name='Liekes')),
                ('comments', models.PositiveIntegerField(verbose_name='Comments')),
                ('shares', models.PositiveIntegerField(verbose_name='Shares')),
                ('clicks', models.PositiveIntegerField(verbose_name='Advert Clicks')),
                ('link_clicks', models.PositiveIntegerField(verbose_name='Link Clicks')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoogleAdWordsStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clicks', models.PositiveIntegerField(verbose_name='Advert Clicks')),
                ('impressions', models.PositiveIntegerField(verbose_name='Advert Impressions')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LinkedinStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('phone_number', models.CharField(default=b'', max_length=16, verbose_name='Phone number', blank=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('email', models.EmailField(max_length=254, verbose_name=b'Correo')),
                ('source', models.PositiveSmallIntegerField(verbose_name='Source', choices=[(1, b'No especificado'), (2, b'Roofmedia'), (3, b'Facebook'), (4, b'GoogleAdWords'), (5, b'Linkedin')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ad', models.ForeignKey(to='content.AdBase')),
            ],
            options={
                'ordering': ('created_at',),
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
                ('ad', models.ForeignKey(to='content.AdBase')),
            ],
            options={
                'ordering': ('created_at',),
                'verbose_name': 'Register',
                'verbose_name_plural': 'Registry',
            },
        ),
        migrations.AddField(
            model_name='linkedinstat',
            name='register',
            field=models.ForeignKey(to='analytics.StatRegister'),
        ),
        migrations.AddField(
            model_name='googleadwordsstat',
            name='register',
            field=models.ForeignKey(to='analytics.StatRegister'),
        ),
        migrations.AddField(
            model_name='facebookstat',
            name='register',
            field=models.ForeignKey(to='analytics.StatRegister'),
        ),
    ]
