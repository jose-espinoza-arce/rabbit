# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.utils.timezone
import mptt.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('url', models.URLField(verbose_name='Advertised URL')),
                ('since', models.DateTimeField(auto_now_add=True, verbose_name='Since')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('start_showing', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start showing')),
                ('stop_showing', models.DateTimeField(default=datetime.datetime(9999, 12, 29, 23, 59, 59, 999999, tzinfo=utc), verbose_name='Stop showing')),
            ],
            options={
                'verbose_name': 'Ad Base',
                'verbose_name_plural': 'Ad Bases',
            },
        ),
        migrations.CreateModel(
            name='AdCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='Description')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='child', blank=True, to='content.AdCategory', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdClick',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('click_date', models.DateTimeField(auto_now_add=True, verbose_name='When')),
                ('source_ip', models.GenericIPAddressField(null=True, verbose_name='Who', blank=True)),
            ],
            options={
                'verbose_name': 'Ad Click',
                'verbose_name_plural': 'Ad Clicks',
            },
        ),
        migrations.CreateModel(
            name='AdImpression',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('impression_date', models.DateTimeField(auto_now_add=True, verbose_name='When')),
                ('source_ip', models.GenericIPAddressField(null=True, verbose_name='Who', blank=True)),
            ],
            options={
                'verbose_name': 'Ad Impression',
                'verbose_name_plural': 'Ad Impressions',
            },
        ),
        migrations.CreateModel(
            name='AdType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'Type',
                'verbose_name_plural': 'Types',
            },
        ),
        migrations.CreateModel(
            name='Advertiser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=255, verbose_name='Company Name')),
                ('website', models.URLField(verbose_name='Company Site')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('company_name',),
                'verbose_name': 'Ad Provider',
                'verbose_name_plural': 'Advertisers',
            },
        ),
        migrations.CreateModel(
            name='AdZone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'Zone',
                'verbose_name_plural': 'Zones',
            },
        ),
        migrations.CreateModel(
            name='BannerAd',
            fields=[
                ('adbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='content.AdBase')),
                ('content', models.ImageField(upload_to=b'adzone/bannerads/', verbose_name='Content')),
            ],
            bases=('content.adbase',),
        ),
        migrations.CreateModel(
            name='TextAd',
            fields=[
                ('adbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='content.AdBase')),
                ('content', models.TextField(verbose_name='Content')),
            ],
            bases=('content.adbase',),
        ),
        migrations.AddField(
            model_name='adimpression',
            name='ad',
            field=models.ForeignKey(to='content.AdBase'),
        ),
        migrations.AddField(
            model_name='adclick',
            name='ad',
            field=models.ForeignKey(to='content.AdBase'),
        ),
        migrations.AddField(
            model_name='adbase',
            name='advertiser',
            field=models.ForeignKey(verbose_name='Ad Provider', to='content.Advertiser'),
        ),
        migrations.AddField(
            model_name='adbase',
            name='category',
            field=models.ForeignKey(verbose_name='Category', blank=True, to='content.AdCategory', null=True),
        ),
        migrations.AddField(
            model_name='adbase',
            name='type',
            field=models.ForeignKey(verbose_name='Type', blank=True, to='content.AdType', null=True),
        ),
    ]
