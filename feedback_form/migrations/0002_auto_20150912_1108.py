# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Correo-e', blank=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.TextField(max_length=4000, verbose_name='Mensaje'),
        ),
    ]
