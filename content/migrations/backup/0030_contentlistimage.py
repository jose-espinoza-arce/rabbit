# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0029_auto_20150831_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentListImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to='content/bannerads/images', verbose_name='List Image')),
                ('main', models.NullBooleanField()),
                ('adbase', models.ForeignKey(related_name='images', to='content.AdBase')),
            ],
        ),
    ]
