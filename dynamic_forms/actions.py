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

from mailqueue.models import MailerMessage


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

@formmodel_action(_('Send confirmation email to posible client of our client'))
def dynamic_form_send_confirmation_email(form_model, form, advert, request):
    from django.template import Template, Context

    #TODO: crear un correo dew confirmación por defecto.
    message = Template(advert.confirmation_email). render(Context({'advert': advert}))

    new_message = MailerMessage()
    new_message.subject = advert.confirmation_email_subject
    new_message.to_address = form.cleaned_data['email']
    new_message.bcc_address = '%s, info@roofmedia.mx' % advert.advertiser.roof_contact #settings.DYNAMIC_FORMS_EMAIL_HIDDEN_RECIPIENTS
    new_message.reply_to = advert.advertiser.email
    new_message.from_address = 'info@roofmedia.mx'
    new_message.from_name = 'Roof Media'
    new_message.content = ""
    new_message.html_content = message
    new_message.app = "dynamic_forms"
    new_message.save()




@formmodel_action(_('Send email to our client'))
def dynamic_form_send_email(form_model, form, advert, request):
    from django.template import Template, Context

    mapped_data = form.get_mapped_data()
    ctx = {
        'form_model': form_model,
        'form': form,
        'data': sorted(mapped_data.items()),
        'advert': advert,
    }
    if advert.notification_email_subject:
        subject = advert.notification_email_subject
    else:
        subject = _('Has recibido una nueva oportunidad de venta')
    if advert.notification_email:
        message = Template(advert.notification_email).render(Context(ctx))
    else:
        message = render_to_string('dynamic_forms/roofmedia_email.txt', ctx)

    new_message = MailerMessage()
    new_message.subject = subject
    new_message.to_address = advert.advertiser.email
    new_message.bcc_address = '%s, info@roofmedia.mx' % advert.advertiser.roof_contact #settings.DYNAMIC_FORMS_EMAIL_HIDDEN_RECIPIENTS
    new_message.from_address = 'info@roofmedia.mx'
    new_message.from_name = 'Roof Media'
    new_message.content = ''
    new_message.html_content = message
    new_message.app = "dynamic_forms"
    new_message.save()




@formmodel_action(_('Store in database'))
def dynamic_form_store_database(form_model, form, advert, request):
    from dynamic_forms.models import FormModelData
    from analytics.models import SaleOportunity


    mapped_data = form.get_mapped_data()
    value = json.dumps(mapped_data, cls=DjangoJSONEncoder)
    data = FormModelData.objects.create(form=form_model, value=value, advert=advert)
    name = form.cleaned_data['name']
    email = form.cleaned_data['email']
    sopt = SaleOportunity(name=name, email=email, form_data=data, ad=advert, source=2)
    if 'phone_number' in form.cleaned_data.keys():
        sopt.phone_number = form.cleaned_data['phone_number']
    sopt.save()
    return data


@formmodel_action(_('Send download email'))
def dynamic_form_send_download_email(form_model, form, advert, request):
    from content.models import DownloadLink
    import hashlib
    import random

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

    from_email = advert.advertiser.email
    if form_model.recipient_email:
        hidden_recipient_list = [form_model.recipient_email]
    else:
        hidden_recipient_list = settings.DYNAMIC_FORMS_EMAIL_HIDDEN_RECIPIENTS

    interested_email = [form.cleaned_data['email']]

    send_mail(subject, '', from_email, interested_email, hidden_recipient_list, html_message=message)

    link.save()
    if not os.path.isdir(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))
    os.symlink(src, dst)