# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebookstat',
            name='register',
            field=models.OneToOneField(to='analytics.StatRegister'),
        ),
        migrations.AlterField(
            model_name='googleadwordsstat',
            name='register',
            field=models.OneToOneField(to='analytics.StatRegister'),
        ),
        migrations.AlterField(
            model_name='linkedinstat',
            name='register',
            field=models.OneToOneField(to='analytics.StatRegister'),
        ),
    ]
