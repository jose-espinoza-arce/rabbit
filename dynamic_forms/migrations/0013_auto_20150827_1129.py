# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dynamic_forms.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_forms', '0012_auto_20150826_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formmodel',
            name='actions',
            field=dynamic_forms.fields.TextMultiSelectField(default='', verbose_name='Actions', choices=[('dynamic_forms.actions.dynamic_form_send_download_email', 'Send download email'), ('dynamic_forms.actions.dynamic_form_send_email', 'Send email to client'), ('dynamic_forms.actions.dynamic_form_store_database', 'Store in database')]),
        ),
    ]
