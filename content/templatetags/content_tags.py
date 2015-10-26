# -*- coding: utf-8 -*-

# © Copyright 2009 Andre Engelbrecht. All Rights Reserved.
# This script is licensed under the BSD Open Source Licence
# Please see the text file LICENCE for more information
# If this script is distributed, it must be accompanied by the Licence

from datetime import datetime
from content.models import AdBase, AdImpression

import re

numeric_test = re.compile("^\d+$")




#-----------------Fix likes templtetags (module->model)-------------------------
from secretballot.models import Vote

from django import template

from likes.utils import can_vote, likes_enabled



#--------------- Override get_queryset of taggir_templatetags


#from django.db import models
from django.db.models import Count

from templatetag_sugar.register import tag
from templatetag_sugar.parser import Name, Variable, Constant, Optional, Model

#from taggit.managers import TaggableManager
from taggit.models import TaggedItem, Tag
#from taggit_templatetags import settings
from django.conf import settings

T_MAX = getattr(settings, 'TAGCLOUD_MAX', 9.0)
T_MIN = getattr(settings, 'TAGCLOUD_MIN', 3.0)

#--------------------------------
register = template.Library()
#----------------------------------

# @register.filter
# def getattribute(value, arg):
#     """Gets an attribute of an object dynamically from a string name"""
#     print(value, arg)
#
#     if hasattr(value, str(arg)):
#         return getattr(value, arg)
#     elif hasattr(value, 'has_key') and value.has_key(arg):
#         return value[arg]
#     elif numeric_test.match(str(arg)) and len(value) > int(arg):
#         return value[int(arg)]
#     else:
#         return settings.TEMPLATE_STRING_IF_INVALID

#register.filter('getattribute', getattribute)

def get_queryset(forvar=None):
    if None == forvar:
        # get all tags
        queryset = Tag.objects.all()
    else:
        # extract app label and model name
        beginning, applabel, model = None, None, None
        try:
            beginning, applabel, model = forvar.rsplit('.', 2)
        except ValueError:
            try:
                applabel, model = forvar.rsplit('.', 1)
            except ValueError:
                applabel = forvar

        # filter tagged items
        if applabel:
            queryset = TaggedItem.objects.filter(content_type__app_label=applabel.lower())
        if model:
            queryset = queryset.filter(content_type__model=model.lower())

        # get tags
        tag_ids = queryset.values_list('tag_id', flat=True)
        queryset = Tag.objects.filter(id__in=tag_ids)
    return queryset.annotate(num_times=Count('taggit_taggeditem_items'))

def get_weight_fun(t_min, t_max, f_min, f_max):
    def weight_fun(f_i, t_min=t_min, t_max=t_max, f_min=f_min, f_max=f_max):
        mult_fac = float(t_max-t_min)/float(f_max-f_min)
        return t_max - (f_max-f_i)*mult_fac
    return weight_fun

@tag(register, [Constant('as'), Name(), Optional([Constant('for'), Variable()])])
def get_taglist(context, asvar, forvar=None):
    queryset = get_queryset(forvar)
    queryset = queryset.order_by('-num_times')
    context[asvar] = queryset
    return ''

@tag(register, [Constant('as'), Name(), Optional([Constant('for'), Variable()])])
def get_tagcloud(context, asvar, forvar=None):
    queryset = get_queryset(forvar)
    num_times = queryset.values_list('num_times', flat=True)
    if(len(num_times) == 0):
        context[asvar] = queryset
        return ''
    weight_fun = get_weight_fun(T_MIN, T_MAX, min(num_times), max(num_times))
    queryset = queryset.order_by('name')
    for tag in queryset:
        tag.weight = weight_fun(tag.num_times)
    context[asvar] = queryset
    return ''

def include_tagcloud(forvar=None):
    return {'forvar': forvar}

def include_taglist(forvar=None):
    return {'forvar': forvar}

register.inclusion_tag('taggit_templatetags/taglist_include.html')(include_taglist)
register.inclusion_tag('taggit_templatetags/tagcloud_include.html')(include_tagcloud)



#A helper for the content type
from django.contrib.contenttypes.models import ContentType

@register.filter
def content_type(obj):
    if not obj:
        return False
    return ContentType.objects.get_for_model(obj)





#-----------Fix likes templte tag (module->model)
@register.inclusion_tag('likes/inclusion_tags/likes_extender.html', takes_context=True)
def adlikes(context, obj, template=None):
    if template is None:
        template = 'likes/inclusion_tags/likes.html'
    request = context['request']
    import_js = False
    if not hasattr(request, '_django_likes_js_imported'):
        setattr(request, '_django_likes_js_imported', 1)
        import_js = True
    context.update({
        'template': template,
        'object': obj,
        'likes_enabled': likes_enabled(obj, request),
        'can_vote': can_vote(obj, request.user, request),
        'content_type': "-".join((obj._meta.app_label, obj._meta.model_name)),
        'import_js': import_js
    })
    return context


#------------------------------------------------------------------------------

@register.tag(name='get_parameters')
def get_parameters(parser, token):
    """
    {% get_parameters except_field %}
    """

    args = token.split_contents()
    if len(args) < 2:
        raise template.TemplateSyntaxError(
            "get_parameters tag takes at least 1 argument")
    return GetParametersNode(args[1].strip())


class GetParametersNode(template.Node):
    """
    Renders current get parameters except for the specified parameter
    """
    def __init__(self, field):
        self.field = field

    def render(self, context):
        request = context['request']
        getvars = request.GET.copy()

        if self.field in getvars:
            del getvars[self.field]

        if len(getvars.keys()) > 0:
            get_params = "%s&" % getvars.urlencode()
        else:
            get_params = ''

        return get_params

@register.inclusion_tag('adzone/ad_tag.html', takes_context=True)
def random_zone_ad(context, ad_zone):
    """
    Returns a random advert for ``ad_zone``.
    The advert returned is independent of the category

    In order for the impression to be saved add the following
    to the TEMPLATE_CONTEXT_PROCESSORS:

    'adzone.context_processors.get_source_ip'

    Tag usage:
    {% load adzone_tags %}
    {% random_zone_ad 'zone_slug' %}

    """
    to_return = {}

    # Retrieve a random ad for the zone
    ad = AdBase.objects.get_random_ad(ad_zone)
    to_return['ad'] = ad

    # Record a impression for the ad
    if 'from_ip' in context and ad:
        from_ip = context.get('from_ip')
        try:
            impression = AdImpression(
                ad=ad, impression_date=datetime.now(), source_ip=from_ip)
            impression.save()
        except:
            pass
    return to_return


@register.inclusion_tag('adzone/ad_tag.html', takes_context=True)
def random_category_ad(context, ad_zone, ad_category):
    """
    Returns a random advert from the specified category.

    Usage:
    {% load adzone_tags %}
    {% random_category_ad 'zone_slug' 'my_category_slug' %}

    """
    to_return = {}

    # Retrieve a random ad for the category and zone
    ad = AdBase.objects.get_random_ad(ad_zone, ad_category)
    to_return['ad'] = ad

    # Record a impression for the ad
    if 'from_ip' in context and ad:
        from_ip = context.get('from_ip')
        try:
            impression = AdImpression(
                ad=ad, impression_date=datetime.now(), source_ip=from_ip)
            impression.save()
        except:
            pass
    return to_return


@register.simple_tag(name='get_video_img')
def get_video_img(video_url):
    video_id = video_url.split('/')[-1]
    img_url = ''

    if 'youtube' in video_url:
        img_url = 'http://img.youtube.com/vi/%s/0.jpg' % video_id
    elif 'vimeo' in video_url:
        import json
        import urllib2
        response = urllib2.urlopen('http://vimeo.com/api/v2/video/%s.json' % video_id)
        json_resp = response.read()
        video_dict = json.loads(json_resp)
        img_url = video_dict[0]['thumbnail_large']

    return img_url

