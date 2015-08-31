# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import warnings
import os

import six
#from django.core.mail import send_mail
from django.core.serializers.json import DjangoJSONEncoder
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from dynamic_forms.conf import settings
from dynamic_forms.utils import is_old_style_action
from dynamic_forms.mail import send_mail


class ActionRegistry(object):

    def __init__(self):
        self._actions = {}

    def get(self, key):
        return self._actions.get(key, None)

    def get_as_choices(self):
        for k, f in sorted(six.iteritems(self._actions)):
            yield k, f.label

    def register(self, func, label):
        if not callable(func):
            raise ValueError('%r must be a callable' % func)

        if is_old_style_action(func):
            warnings.warn('The formmodel action "%s" is missing the third '
                          'argument "request". You should update your code to '
                          'match action(form_model, form, request).' % label,
                          DeprecationWarning)

        func.label = label
        key = '%s.%s' % (func.__module__, func.__name__)
        self._actions[key] = func

    def unregister(self, key):
        if key in self._actions:
            del self._actions[key]


action_registry = ActionRegistry()


def formmodel_action(label):
    def decorator(func):
        action_registry.register(func, label)
        return func
    return decorator


@formmodel_action(_('Send email to client'))
def dynamic_form_send_email(form_model, form, advert, request):
    mapped_data = form.get_mapped_data()

    subject = _('Form “%(formname)s” submitted') % {'formname': form_model}

    message = render_to_string('dynamic_forms/email.txt', {
        'form': form_model,
        'data': sorted(mapped_data.items()),
    })

    from_email = form.cleaned_data['correo']
    if form_model.recipient_email:
        hidden_recipient_list = [form_model.recipient_email]
    else:
        hidden_recipient_list = settings.DYNAMIC_FORMS_EMAIL_RECIPIENTS

    client_email = [advert.advertiser.email]

    send_mail(subject, '', from_email, client_email, hidden_recipient_list, html_message=message)



@formmodel_action(_('Store in database'))
def dynamic_form_store_database(form_model, form, advert, request):
    from dynamic_forms.models import FormModelData
    mapped_data = form.get_mapped_data()
    value = json.dumps(mapped_data, cls=DjangoJSONEncoder)
    data = FormModelData.objects.create(form=form_model, value=value, advert=advert)
    return data


@formmodel_action(_('Send download email'))
def dynamic_form_send_download_email(form_model, form, advert, request):
    from content.models import DownloadLink
    import hashlib, random
    #print form.cleaned_data
    #salt1 = ''.join([str(random.randrange(10)) for i in range(10)])
    salt2 = ''.join(['{0}'.format(random.randrange(10)) for i in range(10)])
    key = hashlib.md5('{0}{1}'.format(salt2, advert.file.name)).hexdigest()

    src = '/'.join([settings.MEDIA_ROOT, advert.file.name])

    download_root = os.path.join(settings.MEDIA_ROOT, 'downloads')
    download_url = os.path.join(settings.MEDIA_URL, 'downloads')

    dst = os.path.join(download_root, key+'.pdf')
    dst_url = os.path.join(download_url, key+'.pdf')
    link = DownloadLink(key=key, ad=advert, url=dst_url, filepath=dst)
    site_url = request.build_absolute_uri('/')
    dl_url = site_url[:-1] + dst_url
    request.META['DL_URL'] = dl_url

    subject = _('Descarga de archivo del anuncio “%(advert)s” submitted') % {'advert': advert.title}

    message = render_to_string('dynamic_forms/download_email.txt', {
        'dl_url': dl_url,
    })

    print advert.advertiser.email
    from_email = advert.advertiser.email
    if form_model.recipient_email:
        hidden_recipient_list = [form_model.recipient_email]
    else:
        hidden_recipient_list = settings.DYNAMIC_FORMS_EMAIL_RECIPIENTS

    interested_email = [form.cleaned_data['correo']]

    send_mail(subject, '', from_email, interested_email, hidden_recipient_list, html_message=message)

    link.save()
    if not os.path.isdir(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))
    os.symlink(src, dst)