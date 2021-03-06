# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import content.models
import mptt.fields
import django.utils.timezone
from django.conf import settings
import django.core.validators


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
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('url', models.URLField(verbose_name='Advertised URL')),
                ('description', models.TextField(max_length=450, verbose_name='Description', blank=True)),
                ('since', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('file', models.FileField(default='', upload_to='content/uploads/', verbose_name='File', blank=True)),
                ('start_showing', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start showing')),
                ('stop_showing', models.DateTimeField(default=content.models.max_datetime, verbose_name='Stop showing')),
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
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='Description')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='child', blank=True, to='content.AdCategory', null=True)),
            ],
            options={
                'verbose_name': 'Ad category',
                'verbose_name_plural': 'Ad categories',
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
            name='AdPhoneView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('view_date', models.DateTimeField(auto_now_add=True, verbose_name='When')),
                ('source_ip', models.GenericIPAddressField(null=True, verbose_name='Who', blank=True)),
            ],
            options={
                'verbose_name': 'Ad Phone View',
                'verbose_name_plural': 'Ad Phone Views',
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
                ('phone_number', models.CharField(default='', max_length=16, verbose_name='Phone number', blank=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
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
            name='ContentListImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to='content/bannerads/images', verbose_name='List Image')),
                ('main', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='DownloadLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=255, verbose_name='Key')),
                ('filepath', models.FilePathField(verbose_name='Link Path')),
                ('since', models.DateTimeField(auto_now_add=True, verbose_name='Since')),
                ('url', models.URLField(verbose_name='Url Path')),
            ],
        ),
        migrations.CreateModel(
            name='BannerAd',
            fields=[
                ('adbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='content.AdBase')),
                ('content', models.ImageField(upload_to='content/bannerads/', verbose_name='Banner')),
                ('content_mobile', models.ImageField(default='', upload_to='content/bannerads/mobile', verbose_name='Mobile Banner', blank=True)),
            ],
            options={
                'verbose_name': 'Banner Ad',
                'verbose_name_plural': 'Banner Ads',
            },
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
        migrations.CreateModel(
            name='VideoAd',
            fields=[
                ('adbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='content.AdBase')),
                ('video_url', models.URLField(verbose_name='Video')),
                ('content', models.ImageField(default='', help_text='This image will be used in the list views.', verbose_name='Image', upload_to='content/videoads/')),
                ('content_mobile', models.ImageField(default='', upload_to='content/videoads/mobile', blank=True, help_text='This image will be used in the list views for mobiles.', verbose_name='Mobile Image')),
            ],
            options={
                'verbose_name': 'Video Ad',
                'verbose_name_plural': 'Video Ads',
            },
            bases=('content.adbase',),
        ),
        migrations.AddField(
            model_name='downloadlink',
            name='ad',
            field=models.ForeignKey(related_name='links', to='content.AdBase'),
        ),
        migrations.AddField(
            model_name='contentlistimage',
            name='adbase',
            field=models.ForeignKey(related_name='images', to='content.AdBase'),
        ),
        migrations.AddField(
            model_name='adphoneview',
            name='ad',
            field=models.ForeignKey(related_name='phone_views', to='content.AdBase'),
        ),
        migrations.AddField(
            model_name='adimpression',
            name='ad',
            field=models.ForeignKey(related_name='impressions', to='content.AdBase'),
        ),
        migrations.AddField(
            model_name='adclick',
            name='ad',
            field=models.ForeignKey(related_name='clicks', to='content.AdBase'),
        ),
    ]
