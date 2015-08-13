# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adzone', '0003_auto_20150811_1549'),
        ('dynamic_forms', '0006_auto_20150811_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='formmodeldata',
            name='bannerad',
            field=models.ForeignKey(related_name='sell_oportunities', default=1, to='adzone.BannerAd'),
            preserve_default=False,
        ),
    ]
