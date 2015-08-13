# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adzone', '0004_advertiser_email'),
        ('dynamic_forms', '0008_auto_20150812_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formmodeldata',
            name='bannerad',
        ),
        migrations.AddField(
            model_name='formmodeldata',
            name='advert',
            field=models.ForeignKey(related_name='sell_opportunities', default=1, to='adzone.AdBase'),
            preserve_default=False,
        ),
    ]
