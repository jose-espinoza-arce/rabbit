# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_forms', '0013_auto_20150827_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formmodel',
            name='success_template',
            field=models.CharField(default='dynamic_forms/form_success.html', max_length=100, verbose_name='Success template path', choices=[(b'dynamic_forms/form_success.html', 'Default success template'), (b'dynamic_forms/myform_success.html', 'My success template'), (b'dynamic_forms/downloadform_success.html', 'Download success template')]),
        ),
    ]
