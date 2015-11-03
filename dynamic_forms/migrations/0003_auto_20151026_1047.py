# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_forms', '0002_auto_20151026_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formmodel',
            name='success_template',
            field=models.CharField(default='dynamic_forms/form_success.html', max_length=100, verbose_name='Success template path', choices=[(b'dynamic_forms/myform_success.html', 'Plantilla de exito por defecto'), (b'dynamic_forms/downloadform_success.html', 'Download success template'), (b'dynamic_forms/taller_redes_form_success.html', 'Plantilla de exito para Taller de redes.')]),
        ),
        migrations.AddField(
            model_name='formmodel',
            name='header',
            field=models.TextField(max_length=255, verbose_name='Header', blank=True),
        ),
    ]
