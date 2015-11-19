from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MailQueueConfig(AppConfig):
    name = 'mailqueue'
    label = 'mailqueue'
    verbose_name = _("Mail Queue")
