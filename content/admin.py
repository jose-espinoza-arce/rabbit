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

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import *
from django.utils.translation import ugettext_lazy as _



class HasRegisterFilter(admin.SimpleListFilter):
    title = _('Has register')
    parameter_name = 'has_filter'

    def lookups(self, request, model_admin):
        return (
            ('0', _('No')),
            ('1', _('Yes')),
        )

    def queryset(self, request, queryset):
        if self.value() == '0':

            q = queryset.filter(stats_register__isnull=True)

            return q
        if self.value() == '1':

            q = queryset.filter(stats_register__isnull=False)

            return q


class MyReadOnlyPaaswordHashWidget(ReadOnlyPasswordHashWidget):

    def render(self, name, value, attrs):
        final_attrs = self.build_attrs(attrs)

        return format_html("<div{}>{}</div>", flatatt(final_attrs), '')

class MyUserAdmin(UserAdmin):

    def __init__(self, model, admin_site):
        self.__class__.form.declared_fields['password'].widget = MyReadOnlyPaaswordHashWidget(attrs=None)
        super(UserAdmin, self).__init__(model, admin_site)

    def get_fieldsets(self, request, obj=None):

        if not request.user.is_superuser:
            self.fieldsets = (
                (None, {'fields': ('username', 'password')}),
                (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
                (_('Permissions'), {'fields': ('is_active', 'is_staff', 'groups')}),
                (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
            )
        else:
            self.fieldsets = (
                (None, {'fields': ('username', 'password')}),
                (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
                (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
                (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
            )

        return super(MyUserAdmin, self).get_fieldsets(request, obj)

    def get_queryset(self, request):
        qs = super(MyUserAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(is_superuser=0)

    def get_list_filter(self, request):
        list_filters = ('is_staff', 'is_active', 'groups')
        if request.user.is_superuser:
            return super(MyUserAdmin, self).get_list_filter(request)
        else:
            return list_filters



admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)

class ContentListImageInline(admin.TabularInline):
    model = ContentListImage
    extra = 3

class AdBaseForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(AdBaseForm, self).clean()
        file = cleaned_data.get('file')
        actionform = cleaned_data.get('actionform')
        download_actionform = None

        download_action_list = [u'dynamic_forms.actions.dynamic_form_send_download_email']
        if actionform:
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
    list_display = ['title', 'since', 'advertiser', 'has_register', 'start_showing', 'stop_showing']
    list_filter = ['stop_showing', HasRegisterFilter]
    search_fields = ['title', 'advertiser__company_name']
    raw_id_fields = ['advertiser']
    form = AdBaseForm
    try:
        clients_group = Group.objects.get(name='Clientes')
    except:
        clients_group = None

    fieldsets = [(None, {'fields': ('title', 'slug', 'category', 'description', 'advertiser', 'url')}),
                    (_('Call to action'), {'fields': ('actionform', 'file')}),
                    (_('Period'), {'fields': ('start_showing', 'stop_showing')})
                ]


    def has_register(self, obj):
        if getattr(obj, 'stats_register', None):
            return _('Yes')
        else:
            return _('No')

    def get_queryset(self, request):
        qs = super(AdBaseAdmin, self).get_queryset(request)
        if self.is_client(request):
            qs = qs.filter(advertiser__user=request.user)
        return qs

    def get_actions(self, request):
        actions = super(AdBaseAdmin, self).get_actions(request)
        if self.is_client(request):
            actions = None
        return actions

    def get_list_display_links(self, request, list_display):
        list_display_links = super(AdBaseAdmin, self).get_list_display_links(request, list_display)
        #if self.is_client(request):
        #    list_display_links = None
        return list_display_links

    #inlines = [ContentListImageInline,]

    def get_changelist(self, request, **kwargs):
        cl = super(AdBaseAdmin, self).get_changelist(request, **kwargs)
        if self.is_client(request):
            class mcl(cl):
                def url_for_result(self, result):
                    pk = getattr(result, self.pk_attname)
                    obj = AdBase.objects.get(pk=pk)
                    return obj.get_absolute_url()
        else:
            mcl = cl
        return mcl

    def is_client(self, request):
        return self.clients_group in request.user.groups.all()


    # def get_form(self, request, obj=None, **kwargs):
    #     """
    #     Overrides the widget for description so it displays as a textarea.
    #     The original field is a CharField because of the 450 max_length requirement;
    #     textarea field don't have max_length attribute.
    #     """
    #     form = super(AdBaseAdmin, self).get_form(request, obj, **kwargs)
    #     #form.base_fields['description'].widget = admin.widgets.AdminTextareaWidget()
    #     return form


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
                                            'impresfmedia.mx/sion_date',
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

    def __init__(self, *args, **kwargs):
        super(AdBaseAdmin, self).__init__(*args, **kwargs)
        self.fieldsets.insert(1,(_('Content'), {'fields': ('content', 'content_mobile')}))

class BannerAdAdmin(AdBaseAdmin):
    search_fields = ['title', 'advertiser__company_name']
    fieldsets = [(None, {'fields': ('title', 'slug', 'category', 'description', 'advertiser', 'url')}),
                 (_('Banner'), {'fields': ('content', 'content_mobile')}),
                 (_('Call to action'), {'fields': ('actionform', 'file')}),
                 (_('Period'), {'fields': ('start_showing', 'stop_showing')}),
                 (_('Tags'), {'fields': ('tags',)}),
                ]


class VideoAdAdmin(AdBaseAdmin):
    search_fields = ['title', 'advertiser__company_name']

    fieldsets = [(None, {'fields': ('title', 'slug', 'category', 'description', 'advertiser', 'url')}),
                 (_('Video'), {'fields': ('content', 'content_mobile', 'video_url')}),
                 (_('Call to action'), {'fields': ('actionform', 'file')}),
                 (_('Period'), {'fields': ('start_showing', 'stop_showing')}),
                 (_('Tags'), {'fields': ('tags',)}),
                ]




admin.site.register(Advertiser, AdvertiserAdmin)

#admin.site.register(AdType, AdTypeAdmin)

admin.site.register(AdBase, AdBaseAdmin)
admin.site.register(AdCategory, AdCategoryAdmin)
#admin.site.register(AdZone, AdZoneAdmin)
#admin.site.register(TextAd, TextAdAdmin)
admin.site.register(BannerAd, BannerAdAdmin)
admin.site.register(VideoAd, VideoAdAdmin)
#admin.site.register(AdPhoneView, AdPhoneViewAdmin)
#admin.site.register(AdClick, AdClickAdmin)
#admin.site.register(AdImpression, AdImpressionAdmin)
