# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import OrderedDict

import six
from django import forms

from dynamic_forms.formfields import formfield_registry


class MultiSelectFormField(forms.MultipleChoiceField):
    # http://djangosnippets.org/snippets/2753/

    widget = forms.CheckboxSelectMultiple

    def __init__(self, *args, **kwargs):
        self.widget = kwargs.pop('widget', self.widget)
        self.separate_values_by = kwargs.pop('separate_values_by', ',')
        super(MultiSelectFormField, self).__init__(*args, **kwargs)

    def clean(self, value):
        if not value and self.required:
            raise forms.ValidationError(self.error_messages['required'])
        return value

    def prepare_value(self, value):
        if isinstance(value, list):
            return value
        return value.split(self.separate_values_by)


class FormModelForm(forms.Form):

    def __init__(self, model, *args, **kwargs):
        self.model = model
        super(FormModelForm, self).__init__(*args, **kwargs)
        self.model_fields = OrderedDict()

        for field in self.model.fields.all():
            self.model_fields[field.name] = field
            field.generate_form_field(self)

        #Add a hidden field to keep track of the advert recipient
        self.fields['advert'] = forms.IntegerField(widget=forms.HiddenInput)

    def get_mapped_data(self, exclude_missing=False):
        """
        Returns an dictionary sorted by the position of the respective field
        in its form.

        :param boolean exclude_missing: If ``True``, non-filled fields (those
            whose value evaluates to ``False`` are not present in the returned
            dictionary. Default: ``False``
        """
        data = self.cleaned_data
        mapped_data = OrderedDict()
        for key, field in six.iteritems(self.model_fields):
            print(key, field)
            df = formfield_registry.get(field.field_type)
            if df and df.do_display_data() and key != 'agree': #Dont save agreement
                name = field.name
                value = data.get(key, None)
                if exclude_missing and not bool(value):
                    continue
                mapped_data[name] = value
        return mapped_data
