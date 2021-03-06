# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import dynamic_forms.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormFieldModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field_type', models.CharField(max_length=255, verbose_name='Type', choices=[('dynamic_forms.contrib.simple_captcha.models.CaptchaField', 'CAPTCHA'), ('dynamic_forms.contrib.simple_captcha.models.NoReCaptchaField', 'NoCreCAPTCHA'), ('dynamic_forms.formfields.BooleanField', 'Boolean'), ('dynamic_forms.formfields.ChoiceField', 'Choices'), ('dynamic_forms.formfields.DateField', 'Date'), ('dynamic_forms.formfields.DateTimeField', 'Date and Time'), ('dynamic_forms.formfields.DynamicPhoneNumberField', 'Phone'), ('dynamic_forms.formfields.EmailField', 'Email'), ('dynamic_forms.formfields.IntegerField', 'Integer'), ('dynamic_forms.formfields.MultiLineTextField', 'Multi Line Text'), ('dynamic_forms.formfields.SingleLineTextField', 'Single Line Text'), ('dynamic_forms.formfields.TimeField', 'Time')])),
                ('label', models.CharField(max_length=255, verbose_name='Label')),
                ('name', models.SlugField(verbose_name='Name', blank=True)),
                ('_options', models.TextField(null=True, verbose_name='Options', blank=True)),
                ('position', models.SmallIntegerField(default=0, verbose_name='Position', blank=True)),
            ],
            options={
                'ordering': ['parent_form', 'position'],
                'verbose_name': 'Form field',
                'verbose_name_plural': 'Form fields',
            },
        ),
        migrations.CreateModel(
            name='FormModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name='Name')),
                ('submit_url', models.CharField(help_text='The full URL path to the form. It should start and end with a forward slash (<code>/</code>).', unique=True, max_length=100, verbose_name='Submit URL')),
                ('success_url', models.CharField(default='', help_text='The full URL path where the user will be redirected after successfully sending the form. It should start and end with a forward slash (<code>/</code>). If empty, the success URL is generated by appending <code>done/</code> to the \u201cSubmit URL\u201d.', max_length=100, verbose_name='Success URL', blank=True)),
                ('actions', dynamic_forms.fields.TextMultiSelectField(default='', verbose_name='Actions', choices=[('dynamic_forms.actions.dynamic_form_send_download_email', 'Send download email'), ('dynamic_forms.actions.dynamic_form_send_email', 'Send email to client'), ('dynamic_forms.actions.dynamic_form_store_database', 'Store in database')])),
                ('form_template', models.CharField(default='dynamic_forms/form.html', max_length=100, verbose_name='Form template path', choices=[(b'dynamic_forms/myform.html', 'Default form template')])),
                ('success_template', models.CharField(default='dynamic_forms/form_success.html', max_length=100, verbose_name='Success template path', choices=[(b'dynamic_forms/myform_success.html', 'Default success template'), (b'dynamic_forms/downloadform_success.html', 'Download success template')])),
                ('allow_display', models.BooleanField(default=False, help_text='Allow a user to view the input at a later time. This requires the \u201cStore in database\u201d action to be active. The sender will be given a unique URL to recall the data.', verbose_name='Allow display')),
                ('recipient_email', models.EmailField(help_text='Email address to send form data.', max_length=254, null=True, verbose_name='Recipient email', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Dynamic form',
                'verbose_name_plural': 'Dynamic forms',
            },
        ),
        migrations.CreateModel(
            name='FormModelData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.TextField(default='', verbose_name='Form data', blank=True)),
                ('submitted', models.DateTimeField(auto_now_add=True, verbose_name='Submitted on')),
                ('display_key', models.CharField(null=True, default=None, max_length=24, blank=True, help_text='A unique identifier that is used to allow users to view their sent data. Unique over all stored data sets.', unique=True, verbose_name='Display key', db_index=True)),
                ('advert', models.ForeignKey(related_name='sell_opportunities', to='content.AdBase')),
                ('form', models.ForeignKey(related_name='data', on_delete=django.db.models.deletion.SET_NULL, to='dynamic_forms.FormModel', null=True)),
            ],
            options={
                'verbose_name': 'Form data',
                'verbose_name_plural': 'Form data',
            },
        ),
        migrations.AddField(
            model_name='formfieldmodel',
            name='parent_form',
            field=models.ForeignKey(related_name='fields', to='dynamic_forms.FormModel'),
        ),
        migrations.AlterUniqueTogether(
            name='formfieldmodel',
            unique_together=set([('parent_form', 'name')]),
        ),
    ]
