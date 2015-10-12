from django.contrib import admin
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.template.response import TemplateResponse
from django.conf.urls import url
from admin_views.admin import AdminViews
from analytics.models import *
from content.admin import AdBaseAdmin, AdBase


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
    model = SaleOportunity

class StatRegisterAdmin(AdminViews):
    raw_id_fields = ('ad',)
    adbaseadmin = AdBaseAdmin(AdBase, AdBaseAdmin)

    # inlines = [
    #     FacebookStatInline, GoogleAdWordsStatInline, LinkedinStatInline,
    #     GooglePlusStatInline, GoogleAnalyticsInline
    # ]

    admin_views = (
                    (_('Statistics'), 'statistics'),
        )

    # def __init__(self, *args, **kwargs):
    #     super(StatRegisterAdmin, self).__init__(*args, **kwargs)

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

        urls += [
            url(r'statistics/(?P<ad_id>\d+)', self.statistic, name='statistic')
        ]

        print(urls)

        return urls

    def statistic(self, request, *args, **kwargs):
        print('args2')
        print(args)
        print('kwargs2')
        print(kwargs)
        template = 'admin/statistic.html'
        context = {'title': _('Statistics'), 'site_url': '/'}
        return TemplateResponse(request, template, context=context)

    def statistics(self, request, *args, **kwargs):
        print('args')
        print(args)
        print('kwargs')
        print(kwargs)
        template = 'admin/statistic.html'
        context = {'title': _('Statistics'), 'site_url': '/'}
        return TemplateResponse(request, template, context=context)

admin.site.register(SaleOportunity)
admin.site.register(StatRegister, StatRegisterAdmin)
