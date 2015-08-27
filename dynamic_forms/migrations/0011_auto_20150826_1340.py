# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_forms', '0010_auto_20150822_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfieldmodel',
            name='field_type',
            field=models.CharField(max_length=255, verbose_name='Type', choices=[('dynamic_forms.contrib.simple_captcha.models.CaptchaField', 'CAPTCHA'), ('dynamic_forms.contrib.simple_captcha.models.NoReCaptchaField', 'NoCreCAPTCHA'), ('dynamic_forms.formfields.BooleanField', 'Boolean'), ('dynamic_forms.formfields.ChoiceField', 'Choices'), ('dynamic_forms.formfields.DateField', 'Date'), ('dynamic_forms.formfields.DateTimeField', 'Date and Time'), ('dynamic_forms.formfields.EmailField', 'Email'), ('dynamic_forms.formfields.IntegerField', 'Integer'), ('dynamic_forms.formfields.MultiLineTextField', 'Multi Line Text'), ('dynamic_forms.formfields.SingleLineTextField', 'Single Line Text'), ('dynamic_forms.formfields.TimeField', 'Time')]),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='success_template',
            field=models.CharField(default='dynamic_forms/form_success.html', max_length=100, verbose_name='Success template path', choices=[(b'dynamic_forms/form_success.html', 'Default success template'), (b'dynamic_forms/myform_success.html', 'My success template')]),
        ),
    ]
