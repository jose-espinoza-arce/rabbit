# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.decorators import classonlymethod
from django.utils.translation import ugettext_lazy as _

from dynamic_forms.formfields import BaseDynamicFormField, dynamic_form_field


#@dynamic_form_field
class CaptchaField(BaseDynamicFormField):

    cls = 'captcha.fields.CaptchaField'
    display_label = _('CAPTCHA')

    class Meta:
        _exclude = ('required',)

    @classonlymethod
    def do_display_data(self):
        return False


@dynamic_form_field
class NoReCaptchaField(BaseDynamicFormField):

    cls = 'nocaptcha_recaptcha.fields.NoReCaptchaField'
    display_label = _('NoCreCAPTCHA')

    class Meta:
        _exclude = ('required',)

    @classonlymethod
    def do_display_data(self):
        return False
