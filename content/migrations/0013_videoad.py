# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_auto_20150813_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoAd',
            fields=[
                ('adbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='content.AdBase')),
                ('content', models.URLField(verbose_name='Content')),
            ],
            bases=('content.adbase',),
        ),
    ]
