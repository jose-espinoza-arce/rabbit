# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_forms', '0005_auto_increase_form_label_max_length_255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formmodel',
            name='form_template',
            field=models.CharField(default='dynamic_forms/form.html', max_length=100, verbose_name='Form template path', choices=[(b'dynamic_forms/form.html', 'Default form template'), (b'dynamic_forms/myform.html', 'My form template')]),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='recipient_email',
            field=models.EmailField(help_text='Email address to send form data.', max_length=254, null=True, verbose_name='Recipient email', blank=True),
        ),
    ]
