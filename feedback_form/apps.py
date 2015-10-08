from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class FeedbackFormConfig(AppConfig):
    name = 'feedback_form'
    verbose_name = _('Feedback')
