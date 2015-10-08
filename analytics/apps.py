from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AnalyticsConfig(AppConfig):
    name = 'analytics'
    verbose_name = _('Analytics')
