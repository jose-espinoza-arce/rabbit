# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six
from django.core.exceptions import ValidationError
from django.db import models
from django.forms import CheckboxSelectMultiple, MultipleChoiceField
from django.forms.widgets import CheckboxFieldRenderer, CheckboxChoiceInput
from django.utils.text import capfirst
from django.utils.html import format_html

from dynamic_forms.forms import MultiSelectFormField


class MyCheckboxChoiceInput(CheckboxChoiceInput):

    def render(self, name=None, value=None, attrs=None, choices=()):
        if self.id_for_label:
            label_for = format_html(' for="{}"', self.id_for_label)
        else:
            label_for = ''
        attrs = dict(self.attrs, **attrs) if attrs else self.attrs
        return format_html(
            '{}<label{}>{}</label>', self.tag(attrs), label_for, self.choice_label
        )

class MyCheckboxFieldRenderer(CheckboxFieldRenderer):
    choice_input_class = MyCheckboxChoiceInput

class MyCheckboxSelectMultiple(CheckboxSelectMultiple):
    renderer = MyCheckboxFieldRenderer



class TextMultiSelectField(six.with_metaclass(models.SubfieldBase,
                                              models.TextField)):
    # http://djangosnippets.org/snippets/2753/

    widget = MyCheckboxSelectMultiple

    def __init__(self, *args, **kwargs):
        self.separate_values_by = kwargs.pop('separate_values_by', '\n')
        super(TextMultiSelectField, self).__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name):
        super(TextMultiSelectField, self).contribute_to_class(cls, name)
        if self.choices:
            def _func(self, fieldname=name):
                return self.separate_values_by.join([
                    self.choices.get(value, value) for value in
                    getattr(self, fieldname)
                ])
            setattr(cls, 'get_%s_display' % self.name, _func)

    def deconstruct(self):
        name, path, args, kwargs = super(TextMultiSelectField, self).deconstruct()
        kwargs['separate_values_by'] = self.separate_values_by
        if kwargs.get('separate_values_by', None) == '\n':
            del kwargs['separate_values_by']
        return name, path, args, kwargs

    def formfield(self, **kwargs):
        # don't call super, as that overrides default widget if it has choices
        defaults = {
            'choices': self.choices,
            'help_text': self.help_text,
            'label': capfirst(self.verbose_name),
            'required': not self.blank,
            'separate_values_by': self.separate_values_by,
        }
        if self.has_default():
            defaults['initial'] = self.get_default()
        defaults.update(kwargs)
        defaults['widget'] = self.widget
        return MultiSelectFormField(**defaults)

    def get_db_prep_value(self, value, connection=None, prepared=False):
        if isinstance(value, six.string_types):
            return value
        elif isinstance(value, list):
            return self.separate_values_by.join(value)

    def get_choices_default(self):
        return self.get_choices(include_blank=False)

    def get_choices_selected(self, arr_choices=''):
        if not arr_choices:
            return False
        chces = []
        for choice_selected in arr_choices:
            chces.append(choice_selected[0])
        return chces

    def get_prep_value(self, value):
        return value

    def to_python(self, value):
        if value is not None:
            return (value if isinstance(value, list) else
                value.split(self.separate_values_by))
        return []

    def validate(self, value, model_instance):
        """
        :param callable convert: A callable to be applied for each choice
        """
        arr_choices = self.get_choices_selected(self.get_choices_default())
        for opt_select in value:
            if opt_select not in arr_choices:
                raise ValidationError(
                    self.error_messages['invalid_choice'] % value)
        return

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

    def get_internal_type(self):
        return "TextField"
