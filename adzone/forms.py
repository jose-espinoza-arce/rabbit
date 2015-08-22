from django import forms
from django.forms.widgets import Input
from django.utils.translation import ugettext_lazy as _

class AdSearchForm(forms.Form):
    q = forms.CharField(
           required=False, label=_('Search'),
           widget=Input({
               "placeholder": _('Search'),
               "tabindex": "1",
               "class": "form-control"
           }))