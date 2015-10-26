# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20151024_1607'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'Ubicaci\xf3n', 'verbose_name_plural': 'Ubicaciones'},
        ),
        migrations.AddField(
            model_name='adbase',
            name='confirmation_email',
            field=models.TextField(default=' ', verbose_name='Correo de confirmaci\xf3n'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adbase',
            name='confirmation_email_subject',
            field=models.CharField(default=' ', max_length=255, verbose_name='Subject de correo.'),
            preserve_default=False,
        ),
    ]
