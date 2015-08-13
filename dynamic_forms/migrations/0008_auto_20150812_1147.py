# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_forms', '0007_formmodeldata_bannerad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formmodeldata',
            name='bannerad',
            field=models.ForeignKey(related_name='sell_opportunities', to='adzone.BannerAd'),
        ),
    ]
