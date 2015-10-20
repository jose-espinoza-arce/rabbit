# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_forms', '0017_auto_20151015_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfieldmodel',
            name='field_type',
            field=models.CharField(max_length=255, verbose_name='Type', choices=[('dynamic_forms.contrib.simple_captcha.models.CaptchaField', 'CAPTCHA'), ('dynamic_forms.contrib.simple_captcha.models.NoReCaptchaField', 'NoCreCAPTCHA'), ('dynamic_forms.formfields.BooleanField', 'Boolean'), ('dynamic_forms.formfields.ChoiceField', 'Choices'), ('dynamic_forms.formfields.DateField', 'Date'), ('dynamic_forms.formfields.DateTimeField', 'Date and Time'), ('dynamic_forms.formfields.DynamicPhoneNumberField', 'Phone'), ('dynamic_forms.formfields.EmailField', 'Email'), ('dynamic_forms.formfields.IntegerField', 'Integer'), ('dynamic_forms.formfields.MultiLineTextField', 'Multi Line Text'), ('dynamic_forms.formfields.SingleLineTextField', 'Single Line Text'), ('dynamic_forms.formfields.TimeField', 'Time')]),
        ),
    ]
