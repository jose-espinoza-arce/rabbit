# -*- coding: utf-8 -*-

# © Copyright 2009 Andre Engelbrecht. All Rights Reserved.
# This script is licensed under the BSD Open Source Licence
# Please see the text file LICENCE for more information
# If this script is distributed, it must be accompanied by the Licence
from __future__ import unicode_literals

import csv

from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from django.http import HttpResponse

from content.models import *

from django import forms


class AdBaseForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(AdBaseForm, self).clean()
        file = cleaned_data.get('file')
        actionform = cleaned_data.get('actionform')

        download_action_list = [u'dynamic_forms.actions.dynamic_form_send_download_email']
        download_actionform = set(actionform.actions).intersection(download_action_list)

        if download_actionform and not file:
            msg = 'Seleccionó un formulario de descarga pero no asigno ningún archivo'
            self.add_error('file', msg)
            self.add_error('actionform', msg)

        return self.cleaned_data


class AdvertiserAdmin(admin.ModelAdmin):
    search_fields = ['company_name', 'website']
    list_display = ['company_name', 'website', 'user']
    raw_id_fields = ['user']


class AdTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {u'slug': [u'title']}
    list_display = [u'title', u'slug']


class AdCategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ['name', 'slug']


class AdZoneAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description']


class AdBaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ['title', 'url', 'advertiser', 'since', 'updated', 'start_showing', 'stop_showing']
    list_filter = ['updated', 'start_showing', 'stop_showing', 'since', 'updated']
    search_fields = ['title', 'url']
    raw_id_fields = ['advertiser']
    form = AdBaseForm

    def get_form(self, request, obj=None, **kwargs):
        """
        Overrides the widget for description so it displays as a textarea.
        The original field is a CharField because of the 450 max_length requirement;
        textarea field don't have max_length attribute.
        """
        form = super(AdBaseAdmin, self).get_form(request, obj, **kwargs)
        #form.base_fields['description'].widget = admin.widgets.AdminTextareaWidget()
        return form


class AdPhoneViewAdmin(admin.ModelAdmin):
    search_fields = ['ad', 'source_ip']
    list_display = ['ad', 'view_date', 'source_ip']
    list_filter = ['view_date']
    date_hierarchy = 'view_date'
    #actions = ['download_clicks']


class AdClickAdmin(admin.ModelAdmin):
    search_fields = ['ad', 'source_ip']
    list_display = ['ad', 'click_date', 'source_ip']
    list_filter = ['click_date']
    date_hierarchy = 'click_date'
    actions = ['download_clicks']

    def download_clicks(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="clicks.csv"'
        writer = csv.writer(response)
        writer.writerow(('Title',
                         'Advertised URL',
                         'Source IP',
                         'Timestamp',
                         'Advertiser ID',
                         'Advertiser name',
                         'Zone'))
        queryset = queryset.select_related('ad', 'ad__advertiser')
        for impression in queryset:
            writer.writerow((impression.ad.title,
                             impression.ad.url,
                             impression.source_ip,
                             impression.click_date.isoformat(),
                             impression.ad.advertiser.pk,
                             impression.ad.advertiser.company_name,
                             impression.ad.zone.title))
        return response
    download_clicks.short_description = "Download selected Ad Clicks"

    def get_queryset(self, request):
        qs = super(AdClickAdmin, self).get_queryset(request)
        return qs.select_related('ad').only('ad__title',
                                            'click_date',
                                            'source_ip')


class AdImpressionAdmin(admin.ModelAdmin):
    search_fields = ['ad', 'source_ip']
    list_display = ['ad', 'impression_date', 'source_ip']
    list_filter = ['impression_date']
    date_hierarchy = 'impression_date'
    actions = ['download_impressions']

    def get_queryset(self, request):
        qs = super(AdImpressionAdmin, self).get_queryset(request)
        return qs.select_related('ad').only('ad__title',
                                            'impression_date',
                                            'source_ip')

    def download_impressions(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="impressions.csv"'
        writer = csv.writer(response)
        writer.writerow(('Title',
                         'Advertised URL',
                         'Source IP',
                         'Timestamp',
                         'Advertiser ID',
                         'Advertiser name',
                         'Zone'))
        queryset = queryset.select_related('ad', 'ad__advertiser')
        for impression in queryset:
            writer.writerow((impression.ad.title,
                             impression.ad.url,
                             impression.source_ip,
                             impression.impression_date.isoformat(),
                             impression.ad.advertiser.pk,
                             impression.ad.advertiser.company_name,
                             impression.ad.zone.title))
        return response
    download_impressions.short_description = "Download selected Ad Impressions"


class TextAdAdmin(AdBaseAdmin):
    search_fields = ['title', 'url', 'content']

class VideoAdAdmin(AdBaseAdmin):
    search_fields = ['title', 'url', 'content']

admin.site.register(Advertiser, AdvertiserAdmin)

admin.site.register(AdType, AdTypeAdmin)

admin.site.register(AdCategory, AdCategoryAdmin)
admin.site.register(AdZone, AdZoneAdmin)
admin.site.register(TextAd, TextAdAdmin)
admin.site.register(BannerAd, AdBaseAdmin)
admin.site.register(VideoAd, VideoAdAdmin)
admin.site.register(AdPhoneView, AdPhoneViewAdmin)
admin.site.register(AdClick, AdClickAdmin)
admin.site.register(AdImpression, AdImpressionAdmin)
