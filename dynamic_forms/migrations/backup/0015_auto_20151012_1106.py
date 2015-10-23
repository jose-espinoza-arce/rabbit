# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_forms', '0014_auto_20150828_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formmodel',
            name='form_template',
            field=models.CharField(default='dynamic_forms/form.html', max_length=100, verbose_name='Form template path', choices=[(b'dynamic_forms/myform.html', 'Default form template')]),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='success_template',
            field=models.CharField(default='dynamic_forms/form_success.html', max_length=100, verbose_name='Success template path', choices=[(b'dynamic_forms/myform_success.html', 'Default success template'), (b'dynamic_forms/downloadform_success.html', 'Download success template')]),
        ),
    ]
