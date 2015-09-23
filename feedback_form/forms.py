"""Forms for the ``feedback_form`` app."""
from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse

#from django_libs.utils_email import send_email

from dynamic_forms.mail import send_mail
from django.template.loader import render_to_string

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    """
    A feedback form with modern spam protection.

    :url: Field to trap spam bots.

    """
    url = forms.URLField(required=False)

    def __init__(self, user=None, url=None, prefix='feedback',
                 content_object=None, *args, **kwargs):
        self.content_object = content_object
        super(FeedbackForm, self).__init__(prefix='feedback', *args, **kwargs)
        if url:
            self.instance.current_url = url
        if user:
            self.instance.user = user
            del self.fields['email']
        else:
            self.fields['email'].required = True

    def save(self):
        if not self.cleaned_data.get('url'):
            self.instance.content_object = self.content_object
            obj = super(FeedbackForm, self).save()
            subject = render_to_string('feedback_form/email/subject.txt')
            message = render_to_string('feedback_form/email/body.txt', {'feedback': obj})
            managers = [manager for manager in settings.MANAGERS]

            send_mail(subject, ' ', settings.DEFAULT_FROM_EMAIL, managers, [], html_message=message)
            if getattr(settings, 'FEEDBACK_EMAIL_CONFIRMATION', False):
                email = None
                if obj.email:
                    email = obj.email
                elif obj.user.email:
                    email = obj.user.email
                if email:
                    confirmation_subject = render_to_string('feedback_form/email/confirmation_subject.txt')
                    confirmation_body = render_to_string('feedback_form/email/confirmation_body.txt', {})
                    send_mail(confirmation_subject, '',
                              settings.FROM_EMAIL, [email], html_message=confirmation_body)
            return obj

    class Media:
        css = {'all': ('feedback_form/css/feedback_form.css'), }
        js = ('feedback_form/js/feedback_form.js', )

    class Meta:
        model = Feedback
        fields = ('email', 'message')
