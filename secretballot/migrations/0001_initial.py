# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=50)),
                ('vote', models.SmallIntegerField(choices=[(1, b'+1'), (-1, b'-1')])),
                ('object_id', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(db_index=True, auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(db_index=True, auto_now=True, null=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('token', 'content_type', 'object_id')]),
        ),
    ]
