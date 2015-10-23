# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_forms', '0001_initial'),
        ('taggit', '0002_auto_20150616_2121'),
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adbase',
            name='actionform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Call to action', to='dynamic_forms.FormModel', null=True),
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
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='adbase',
            name='type',
            field=models.ForeignKey(verbose_name='Type', blank=True, to='content.AdType', null=True),
        ),
    ]
