# -*- coding: utf-8 -*-

# © Copyright 2009 Andre Engelbrecht. All Rights Reserved.
# This script is licensed under the BSD Open Source Licence
# Please see the text file LICENCE for more information
# If this script is distributed, it must be accompanied by the Licence

import datetime

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from mptt.models import MPTTModel, TreeForeignKey

from adzone.managers import AdManager

from dynamic_forms.models import FormModel

from taggit.managers import TaggableManager

from django.contrib.sites.models import Site

# Use a datetime a few days before the max to that timezone changes don't
# cause an OverflowError.
MAX_DATETIME = datetime.datetime.max - datetime.timedelta(days=2)
try:
    from django.utils.timezone import now, make_aware, utc
except ImportError:
    now = datetime.datetime.now
else:
    MAX_DATETIME = make_aware(MAX_DATETIME, utc)


class Advertiser(models.Model):
    """ A Model for our Advertiser.  """
    company_name = models.CharField(
        verbose_name=_(u'Company Name'), max_length=255)
    website = models.URLField(verbose_name=_(u'Company Site'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(verbose_name=_('Phone number'), validators=[phone_regex], max_length=16, blank=True, default='')
    email = models.EmailField(_('Email'))

    class Meta:
        verbose_name = _(u'Ad Provider')
        verbose_name_plural = _(u'Advertisers')
        ordering = ('company_name',)

    def __str__(self):
        return self.company_name

    def get_website_url(self):
        return self.website

class AdType(models.Model):
    """
    A model to hold the different types for adverts
    """
    title = models.CharField(verbose_name=_(u'Title'), max_length=255)
    slug = models.SlugField(verbose_name=_(u'Slug'), unique=True)
    description = models.TextField(verbose_name=_(u'Description'))

    class Meta:
        verbose_name = _('Type')
        verbose_name_plural = _('Types')
        ordering = ('title',)

    def __str__(self):
        return self.title






class AdCategory(MPTTModel):
    """ a Model to hold the from taggit.managers import TaggableManagerdifferent Categories for adverts """
    name = models.CharField(verbose_name=_(u'Name'), max_length=255)
    slug = models.SlugField(verbose_name=_(u'Slug'), unique=True)
    description = models.TextField(verbose_name=_(u'Description'))
    parent = TreeForeignKey('self', blank=True, null=True, related_name='child')

    def __init__(self, *args, **kwargs):
        super(AdCategory, self).__init__(*args, **kwargs)



    class MPTTMeta:
        order_insertion_by = ['name']
        unique_together = ('slug', 'parent')

    # class Meta:
    #     verbose_name = _('Category')
    #     verbose_name_plural = _('Categories')
    #     ordering = ('title',)

    def __str__(self):
        return self.name

    def my_get_path(self):
        return '/'.join([getattr(item, 'slug') for item in self.get_ancestors(include_self=True)])


class AdZone(models.Model):
    """ a Model that describes the attributes and behaviours of ad zones """
    title = models.CharField(verbose_name=_(u'Title'), max_length=255)
    slug = models.SlugField(verbose_name=_(u'Slug'))
    description = models.TextField(verbose_name=_(u'Description'))

    class Meta:
        verbose_name = 'Zone'
        verbose_name_plural = 'Zones'
        ordering = ('title',)

    def __str__(self):
        return self.title


class AdBase(models.Model):
    """
    This is our base model, from which all ads will inherit.
    The manager methods for this model will determine which ads to
    display return etc.
    """
    title = models.CharField(verbose_name=_(u'Title'), max_length=255)
    slug = models.SlugField(verbose_name=_(u'Slug'), unique=True)
    url = models.URLField(verbose_name=_(u'Advertised URL'))
    description = models.CharField(verbose_name=_('Description'), blank=True, max_length=450)
    since = models.DateTimeField(verbose_name=_(u'Since'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_(u'Updated'), auto_now=True)
    file = models.FileField(verbose_name=_(u'File'), upload_to='adzone/uploads/',
                             blank=True, default='')

    start_showing = models.DateTimeField(verbose_name=_(u'Start showing'),
                                         default=now)
    stop_showing = models.DateTimeField(verbose_name=_(u'Stop showing'),
                                        default=MAX_DATETIME)

    # Relations
    advertiser = models.ForeignKey(Advertiser, verbose_name=_("Ad Provider"))
    category = models.ForeignKey(AdCategory, verbose_name=_("Category"), blank=True, null=True)
    type = models.ForeignKey(AdType, verbose_name=_(u'Type'), blank=True, null=True)
    # zone = models.ForeignKey(AdZone, verbose_name=_("Zone"))

    actionform = models.ForeignKey(FormModel, verbose_name=_('Call to action'))

    # Our Custom Manager
    objects = AdManager()

    tags = TaggableManager()



    #sites = models.ManyToManyField(Site, verbose_name=(u"Sites"))

    class Meta:
        verbose_name = _('Ad Base')
        verbose_name_plural = _('Ad Bases')

    def __str__(self):
        return self.title

    def get_path(self):
        return self.category.my_get_path() + '/ad/' + self.slug

    @models.permalink
    def get_absolute_url(self):
        return ('adzone_ad_view', [self.id])

    def get_ad_content(self):
        return self.content


class AdImpression(models.Model):
    """
    The AdImpression Model will record every time the ad detail is loaded
    """
    impression_date = models.DateTimeField(
        verbose_name=_(u'When'), auto_now_add=True)
    source_ip = models.GenericIPAddressField(
        verbose_name=_(u'Who'), null=True, blank=True)
    ad = models.ForeignKey(AdBase, related_name='impressions')

    class Meta:
        verbose_name = _('Ad Impression')
        verbose_name_plural = _('Ad Impressions')


class AdClick(models.Model):
    """
    The AdClick model will record every click that an ad gets
    """
    click_date = models.DateTimeField(
        verbose_name=_(u'When'), auto_now_add=True)
    source_ip = models.GenericIPAddressField(
        verbose_name=_(u'Who'), null=True, blank=True)
    ad = models.ForeignKey(AdBase)

    class Meta:
        verbose_name = _('Ad Click')
        verbose_name_plural = _('Ad Clicks')


class AdPhoneView(models.Model):
    """
    The AdPhoneView model will record every phone view that an ad gets
    """
    view_date = models.DateTimeField(
        verbose_name=_(u'When'), auto_now_add=True)
    source_ip = models.GenericIPAddressField(
        verbose_name=_(u'Who'), null=True, blank=True)
    ad = models.ForeignKey(AdBase)

    class Meta:
        verbose_name = _('Ad Phone View')
        verbose_name_plural = _('Ad Phone Views')


# Example Ad Types
class TextAd(AdBase):
    """ A most basic, text based advert """
    content = models.TextField(verbose_name=_(u'Content'))


class BannerAd(AdBase):
    """ A standard banner Ad """
    content = models.ImageField(
        verbose_name=_(u'Content'), upload_to="adzone/bannerads/")
    content_mobile = models.ImageField(
        verbose_name=_(u'Mobile Content'), upload_to="adzone/bannerads/mobile", blank=True, default='')


class VideoAd(AdBase):
    """ A standard video ad """
    video_url = models.URLField(verbose_name=_(u'Url'))
    content = models.ImageField(
        verbose_name=_(u'Content'), upload_to="adzone/videoads/", default='')
    content_mobile = models.ImageField(
        verbose_name=_(u'Mobile Content'), upload_to="adzone/videoads/mobile", blank=True, default='')

    def save(self, *args, **kwargs):
        if 'youtube' in self.content:
            self.content = self.content.replace('watch?v=', 'embed/')
        if 'vimeo' in self.content:
            self.content = 'https://player.vimeo.com/video/' + self.content.split('/')[-1]
        super(VideoAd, self).save(*args, **kwargs)


class DownloadLink(models.Model):
    key = models.CharField(verbose_name=_(u'Key'), max_length=255)
    filepath = models.FilePathField(verbose_name=_(u'Link Path'))
    since = models.DateTimeField(verbose_name=_(u'Since'), auto_now_add=True)
    url = models.URLField(verbose_name=_(u'Url Path'))
    ad = models.ForeignKey(AdBase, related_name='links')

    def delete(self, using=None):
        import os
        try:
            os.remove(self.filepath)
        except OSError:
            pass
        super(DownloadLink, self).delete(using)