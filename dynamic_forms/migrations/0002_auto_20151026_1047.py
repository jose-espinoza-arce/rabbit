# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dynamic_forms.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formmodel',
            name='actions',
            field=dynamic_forms.fields.TextMultiSelectField(default='', verbose_name='Actions', choices=[('dynamic_forms.actions.dynamic_form_send_confirmation_email', 'Send confirmation email to posible client of our client'), ('dynamic_forms.actions.dynamic_form_send_download_email', 'Send download email'), ('dynamic_forms.actions.dynamic_form_send_email', 'Send email to our client'), ('dynamic_forms.actions.dynamic_form_store_database', 'Store in database')]),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='success_template',
            field=models.CharField(default='dynamic_forms/form_success.html', max_length=100, verbose_name='Success template path', choices=[(b'dynamic_forms/myform_success.html', 'Plantilla de exito por defecto')]),
        ),
    ]
