# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0007_auto_20151012_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebookstat',
            name='register',
            field=models.OneToOneField(related_name='facebook_stats', to='analytics.StatRegister'),
        ),
        migrations.AlterField(
            model_name='googleadwordsstat',
            name='register',
            field=models.OneToOneField(related_name='googleadword_stats', to='analytics.StatRegister'),
        ),
        migrations.AlterField(
            model_name='googleanalytics',
            name='register',
            field=models.OneToOneField(related_name='googlean_stats', to='analytics.StatRegister'),
        ),
        migrations.AlterField(
            model_name='googleplusstat',
            name='register',
            field=models.OneToOneField(related_name='googleplus_stats', to='analytics.StatRegister'),
        ),
        migrations.AlterField(
            model_name='linkedinstat',
            name='register',
            field=models.OneToOneField(related_name='linkedin_stats', to='analytics.StatRegister'),
        ),
        migrations.AlterField(
            model_name='statregister',
            name='ad',
            field=models.OneToOneField(related_name='stat_register', to='content.AdBase'),
        ),
        migrations.AlterField(
            model_name='videostat',
            name='register',
            field=models.OneToOneField(related_name='video_stats', to='analytics.StatRegister'),
        ),
    ]
