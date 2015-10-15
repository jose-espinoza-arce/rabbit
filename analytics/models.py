from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from django.utils.encoding import python_2_unicode_compatible


from content.models import AdBase
from dynamic_forms.models import FormModelData

@python_2_unicode_compatible
class SaleOportunity(models.Model):

    CHOICES = (
        (1, 'No especificado'),
        (2, 'Roofmedia'),
        (3, 'Facebook'),
        (4, 'GoogleAdWords'),
        (5, 'Linkedin'),
    )
    ad = models.ForeignKey(AdBase, related_name='sales_oportunities')
    form_data = models.OneToOneField(FormModelData, blank=True)
    name = models.CharField(verbose_name=_('Client Name'), max_length=255)
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
        return 'Client: {0}, Advertiser: {1}'.format(self.name, self.ad.advertiser)

@python_2_unicode_compatible
class StatRegister(models.Model):
    ad = models.OneToOneField(AdBase, related_name='stats_register')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Register')
        verbose_name_plural = 'Registry'
        ordering = ('created_at',)

    def __str__(self):
        return self.ad.title

def upload_path_handler(instance, filename):
    import os.path
    fn, ext = os.path.splitext(filename)
    model_name = instance.__class__.__name__.lower()
    register_id = instance.register.ad.slug
    return "analytics/images/{register}/{model}s/{id}{ext}".format(model=model_name,
                                                                  register=register_id,
                                                                  id=instance.pk, ext=ext)

@python_2_unicode_compatible
class FacebookStat(models.Model):
    register = models.OneToOneField(StatRegister, related_name='facebook_stats')
    fbpostid = models.CharField(verbose_name=_('Post ID'), max_length=255)
    image = models.ImageField(verbose_name=_('Facebook Image'), upload_to=upload_path_handler, blank=True)
    reached = models.PositiveIntegerField(verbose_name=_('Reached people'))
    likes = models.PositiveIntegerField(verbose_name=_('Likes'))
    comments = models.PositiveIntegerField(verbose_name=_('Comments'))
    shares = models.PositiveIntegerField(verbose_name=_('Shares'))
    clicks = models.PositiveIntegerField(verbose_name=_('Advert Clicks'))
    link_clicks = models.PositiveIntegerField(verbose_name=_('Link Clicks'), blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.register.__str__()

@python_2_unicode_compatible
class LinkedinStat(models.Model):
    register = models.OneToOneField(StatRegister, related_name='linkedin_stats')
    lnkpostid = models.CharField(verbose_name=_('Post ID'), max_length=255)
    image = models.ImageField(verbose_name=_('Linkedin Image'), upload_to=upload_path_handler, blank=True)
    reached = models.PositiveIntegerField(verbose_name=_('Linkedin Members'))
    clicks = models.PositiveIntegerField(verbose_name=_('Advert Clicks'))
    impressions = models.PositiveIntegerField(verbose_name=_('Advert Impressions'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.register.__str__()

@python_2_unicode_compatible
class GoogleAdWordsStat(models.Model):
    register = models.OneToOneField(StatRegister, related_name='googleadword_stats')
    adsgroupid = models.CharField(verbose_name=_('Ad Group ID'), max_length=255)
    clicks = models.PositiveIntegerField(verbose_name=_('Advert Clicks'))
    impressions = models.PositiveIntegerField(verbose_name=_('Advert Impressions'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.register.__str__()

@python_2_unicode_compatible
class GooglePlusStat(models.Model):
    register = models.OneToOneField(StatRegister, related_name='googleplus_stats')
    gpidpost = models.CharField(verbose_name=_('Post ID'), max_length=255)
    reached = models.PositiveIntegerField(verbose_name=_('Gplus scope'))
    pluses = models.PositiveIntegerField(verbose_name=_('Pluses(+1)'))
    comments = models.PositiveIntegerField(verbose_name=_('Comments'))
    impressions = models.PositiveIntegerField(verbose_name=_('Advert Impressions'))
    shares = models.PositiveIntegerField(verbose_name=_('Shares'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.register.__str__()

@python_2_unicode_compatible
class GoogleAnalytics(models.Model):
    register = models.OneToOneField(StatRegister, related_name='googlean_stats')
    visitors = models.PositiveIntegerField(verbose_name=_('Visitors'))
    users = models.PositiveIntegerField(verbose_name=_('Users'))
    averagetime = models.PositiveIntegerField(verbose_name=_('Average time(mins)'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.register.__str__()

@python_2_unicode_compatible
class VideoStat(models.Model):
    register = models.OneToOneField(StatRegister, related_name='video_stats')
    plays = models.PositiveIntegerField(verbose_name=_('Times played'))

    def __str__(self):
        return self.register.__str__()


from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

_UNSAVED_FILEFIELD = 'unsaved_filefield'

@receiver(pre_save)
def skip_saving_file(sender, instance, **kwargs):
    list_of_models = ('FacebookStat', 'LinkedinStat')
    if sender.__name__ in list_of_models:
        if not instance.pk and not hasattr(instance, _UNSAVED_FILEFIELD):
            setattr(instance, _UNSAVED_FILEFIELD, instance.image)
            instance.image = None

@receiver(post_save)
def save_file(sender, instance, created, **kwargs):
    list_of_models = ('FacebookStat', 'LinkedinStat')
    if sender.__name__ in list_of_models:
        if created and hasattr(instance, _UNSAVED_FILEFIELD):
            instance.image = getattr(instance, _UNSAVED_FILEFIELD)
            instance.save()
        # delete it if you feel uncomfortable...
        # instance.__dict__.pop(_UNSAVED_FILEFIELD)

