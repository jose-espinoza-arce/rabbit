from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from django.utils.encoding import python_2_unicode_compatible


from content.models import AdBase

@python_2_unicode_compatible
class SaleOportunity(models.Model):

    CHOICES = (
        (1, 'No especificado'),
        (2, 'Roofmedia'),
        (3, 'Facebook'),
        (4, 'GoogleAdWords'),
        (5, 'Linkedin'),
    )
    ad = models.ForeignKey(AdBase)
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(verbose_name=_('Phone number'), validators=[phone_regex], max_length=16, blank=True, default='')
    email = models.EmailField('Correo')
    source = models.PositiveSmallIntegerField(verbose_name=_('Source'), choices=CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Oportunidad de venta'
        verbose_name_plural = 'Oportunidades de venta'
        ordering = ('created_at',)

    def __str__(self):
        return _('Client: %s, Advertiser: %s') % (self.ad.advertiser, self.name)

@python_2_unicode_compatible
class StatRegister(models.Model):
    ad = models.ForeignKey(AdBase)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Register')
        verbose_name_plural = 'Registry'
        ordering = ('created_at',)

    def __str__(self):
        return self.ad.title


@python_2_unicode_compatible
class FacebookStat(models.Model):
    register = models.OneToOneField(StatRegister)
    reached = models.PositiveIntegerField(verbose_name=_('Reached people'))
    likes = models.PositiveIntegerField(verbose_name=_('Liekes'))
    comments = models.PositiveIntegerField(verbose_name=_('Comments'))
    shares = models.PositiveIntegerField(verbose_name=_('Shares'))
    clicks = models.PositiveIntegerField(verbose_name=_('Advert Clicks'))
    link_clicks = models.PositiveIntegerField(verbose_name=_('Link Clicks'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.regitry.__str__()

@python_2_unicode_compatible
class LinkedinStat(models.Model):
    register = models.OneToOneField(StatRegister)
    reached = models.PositiveIntegerField(verbose_name=_('Linkedin Members'))
    clicks = models.PositiveIntegerField(verbose_name=_('Advert Clicks'))
    impressions = models.PositiveIntegerField(verbose_name=_('Advert Impressions'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.regitry.__str__()

@python_2_unicode_compatible
class GoogleAdWordsStat(models.Model):
    register = models.OneToOneField(StatRegister)
    clicks = models.PositiveIntegerField(verbose_name=_('Advert Clicks'))
    impressions = models.PositiveIntegerField(verbose_name=_('Advert Impressions'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.regitry.__str__()

