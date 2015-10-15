from django.contrib import admin
from django.contrib.admin.utils import quote
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.utils.translation import ugettext_lazy as _
from django.template.response import TemplateResponse
from django.conf.urls import url
from functools import update_wrapper
from admin_views.admin import AdminViews
from analytics.models import *
from content.admin import AdBaseAdmin, AdBase


class AdBaseStatAdmin(AdBaseAdmin):
    change_list_template = 'admin/statistic.html'
    actions_on_top = False
    actions_on_bottom = False
    actions = None
    list_display = ['title', 'advertiser', 'start_showing', 'stop_showing']
    search_fields = ['title', 'advertiser__company_name']

    def get_changelist(self, request, **kwargs):
        """
        Returns the ChangeList class for use on the changelist page.
        """
        from django.contrib.admin.views.main import ChangeList


        class StatList(ChangeList):

            def url_for_result(self, result):
                pk = getattr(result, self.pk_attname)
                res_url = reverse('admin:statistic', #% (self.opts.app_label,   self.opts.model_name),
                       args=(quote(pk),),
                       current_app=self.model_admin.admin_site.name)
                return res_url

        return StatList


class FacebookStatInline(admin.StackedInline):
    model = FacebookStat

class LinkedinStatInline(admin.StackedInline):
    model = LinkedinStat

class GoogleAdWordsStatInline(admin.StackedInline):
    model = GoogleAdWordsStat

class VideoStatInline(admin.StackedInline):
    model = VideoStat

class GoogleAnalyticsInline(admin.StackedInline):
    model = GoogleAnalytics

class GooglePlusStatInline(admin.StackedInline):
    model = GooglePlusStat

class SaleOportunityAdmin(admin.ModelAdmin):
    raw_id_fields = ['ad']
    exclude = ['form_data']
    list_display = ['id', 'ad', 'name', 'email', 'phone_number', 'form_data']
    search_fields = ['id', 'ad',]

class StatRegisterAdmin(AdminViews):
    raw_id_fields = ('ad',)
    adbaseadmin = AdBaseStatAdmin(AdBase, admin.site)


    admin_views = (
                    (_('Statistics'), 'statistics'),
        )

    def get_inline_instances(self, request, obj=None):
        print('inline instances')
        #print(getattr(obj.ad, 'videoad', False))
        if getattr(obj, 'ad', False):
            if getattr(obj.ad, 'videoad', False):
                self.inlines = [
                    FacebookStatInline, GoogleAdWordsStatInline, LinkedinStatInline,
                    GooglePlusStatInline, GoogleAnalyticsInline, VideoStatInline
                ]
            else:
                self.inlines = [
                    FacebookStatInline, GoogleAdWordsStatInline, LinkedinStatInline,
                    GooglePlusStatInline, GoogleAnalyticsInline
                ]

        return super(StatRegisterAdmin, self).get_inline_instances(request, obj)

    def get_urls(self):
        urls = super(StatRegisterAdmin,self).get_urls()

        urls.insert(0, url(r'statistics/(?P<ad_id>\d+)/$', self.statistic, name='statistic'))#self.admin_site.admin_view(self.statistic)

        return urls

    def statistic(self, request, ad_id):
        ad = AdBase.objects.filter(pk=ad_id).annotate(views=Count('impressions', distinct=True),
                                                   clics=Count('clicks', distinct=True),
                                                   ph_views=Count('phone_views', distinct=True))[0]
        is_active = ad.is_active()
        ad_url = request.build_absolute_uri(reverse('content:ad_categories', args=[ad.get_path()]))
        ad_register = getattr(ad, 'stats_register', None)
        linkedin = None
        googleplus = None
        googleadword = None
        googlean = None
        video_stats = None
        facebook = None
        if ad_register:
            linkedin = getattr(ad_register, 'linkedin_stats', None)
            googleplus = getattr(ad_register, 'googleplus_stats', None)
            googleadword = getattr(ad_register, 'googleadword_stats', None)
            googlean = getattr(ad_register, 'googlean_stats', None)
            video_stats = getattr(ad_register, 'video_stats', None)
            facebook = getattr(ad_register, 'facebook_stats', None)
        video_url = None
        if ad.videoad:
            if 'youtube' in ad.videoad.video_url:
                video_url = ad.videoad.video_url.replace('embed/', 'watch?v=')
            if 'vimeo' in ad.videoad.video_url:
                video_url = 'https://vimeo.com/' + ad.videoad.video_url.split('/')[-1]

        template = 'admin/statistic_result.html'
        context = dict(
            self.admin_site.each_context(request),
            title= ad.title,
            ad=ad,
            facebook=facebook,
            linkedin=linkedin,
            googleplus=googleplus,
            googleadword=googleadword,
            googlean=googlean,
            video_stats=video_stats,
            is_active=is_active,
            ad_url=ad_url,
            video_url=video_url,
        )
        return TemplateResponse(request, template, context)

    def statistics(self, request, *args, **kwargs):

        context = dict(
            title=_('Statistics'),
            module_name='analytics'
        )
        return self.adbaseadmin.changelist_view(request, extra_context=context)#TemplateResponse(request, template, context)

admin.site.register(SaleOportunity, SaleOportunityAdmin)
admin.site.register(StatRegister, StatRegisterAdmin)
