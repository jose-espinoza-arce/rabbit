# -*- coding: utf-8 -*-

# © Copyright 2009 Andre Engelbrecht. All Rights Reserved.
# This script is licensed under the BSD Open Source Licence
# Please see the text file LICENCE for more information
# If this script is distributed, it must be accompanied by the Licence

from django.db.models import Count
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView
from django.http import Http404

from django.contrib import messages
from django.utils import timezone
import json

from content.models import AdBase, AdClick, AdBase, AdImpression, AdPhoneView
from django.shortcuts import get_object_or_404, redirect

from taggit.models import Tag

from content.forms import AdSearchForm


class AdListView(ListView):
    model = AdBase
    paginate_by = 10

    def get_context_data(self, **kwargs):
        ctx = super(AdListView, self).get_context_data(**kwargs)
        slugs = self.request.path.split('/')
        q = ''

        if 'instance' in kwargs.keys():
            ctx['category'] = kwargs['instance']

        if 'tags' in slugs:
            slugs.pop(0)
            slugs.pop(0)
            names = [tag.name for tag in [Tag.objects.get(slug=slug) for slug in slugs]]
            q = (', ').join(names) + ', '

        ctx['search_form'] = AdSearchForm(initial={'q': q})
        return ctx

    def get_queryset(self):
        qs = super(AdListView, self).get_queryset()
        qs = qs.filter(start_showing__lte=timezone.now(),
                       stop_showing__gte=timezone.now(),).order_by('-pk')

        return qs

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        request.META["CSRF_COOKIE_USED"] = True

        if 'path' in kwargs.keys():
            if 'instance' in kwargs.keys():
                descendants = kwargs['instance'].get_descendants(include_self=True)
                self.queryset = queryset.filter(category__in=descendants)
            elif 'tags' in kwargs.keys():
                self.queryset = queryset.filter(tags__in=kwargs['tags']).distinct()
            else:
                return redirect('content:ad_list')

        self.object_list = self.get_queryset()
        count = self.object_list.count()

        if not request.is_ajax() and not request.path == '/': #reverse()
            if count > 1:
                message = 'Se encontraron %d resultados.' % self.object_list.count()
                messages.add_message(request, messages.INFO, message)
            elif count == 1:
                message = 'Se encontró %d resultado.' % self.object_list.count()
                messages.add_message(request, messages.INFO, message)
            elif count == 0:
                message = 'No se encontraron resultados.'
                messages.add_message(request, messages.ERROR, message)


        allow_empty = self.get_allow_empty()

        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if (self.get_paginate_by(self.object_list) is not None
                    and hasattr(self.object_list, 'exists')):
                is_empty = not self.object_list.exists()
            else:
                is_empty = len(self.object_list) == 0
            if is_empty:
                raise Http404(_("Empty list and '%(class_name)s.allow_empty' is False.")
                        % {'class_name': self.__class__.__name__})

        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class AdDetailView(DetailView):
    model = AdBase

    def get_context_data(self, **kwargs):
        ctx = super(AdDetailView, self).get_context_data(**kwargs)
        ctx['search_form'] = AdSearchForm()
        return ctx

    def get(self, request, *args, **kwargs):
        request.META["CSRF_COOKIE_USED"] = True

        if 'instance' not in kwargs.keys():
            return redirect('content:ad_list')

        try:
            impression = AdImpression(
                ad=self.get_object(),
                impression_date=timezone.now(),
                source_ip=request.META.get('REMOTE_ADDR'),
            )
            impression.save()
        except:
            pass

        self.object = self.get_object()
        context = self.get_context_data(object=self.object, category=self.object.category)

        return self.render_to_response(context)



def ad_view(request, pk):
    """ Record the click in the database, then redirect to ad url """
    ad = get_object_or_404(AdBase, id=pk)

    click = AdClick.objects.create(
        ad=ad,
        click_date=timezone.now(),
        source_ip=request.META.get('REMOTE_ADDR', '')
    )
    click.save()

    redirect_url = ad.url
    if not redirect_url.startswith('http://') and not redirect_url.startswith('https://'):
        # Add http:// to the url so that the browser redirects correctly
        redirect_url = 'http://' + redirect_url

    return HttpResponseRedirect(redirect_url)


def ad_phone_view(request):
    if request.is_ajax():
        if request.method == 'POST':

            pk = request.POST['pk']
            ad = get_object_or_404(AdBase, id=pk)

            phone_view = AdPhoneView.objects.create(
                ad=ad,
                view_date=timezone.now(),
                source_ip=request.META.get('REMOTE_ADDR', ''),
            )

            phone_view.save()
        message = "Yes, AJAX!"
    else:
        message = "Not Ajax"
    return HttpResponse(message)

def tag_hint(request):

    q = request.GET['q']

    results = []
    if len(q) > 2:
        tag_qs = Tag.objects.filter(name__icontains=q)

        annotated_qs = tag_qs.filter(adbase__start_showing__lte=timezone.now(),
                                     adbase__stop_showing__gte=timezone.now())\
                             .annotate(count=Count('taggit_taggeditem_items__id', distinct=True))

        for obj in annotated_qs.order_by('-count', 'slug')[:10]:
            results.append({
                'tag': obj.name,
                'count': obj.count,
            })

    return JsonResponse(results, safe=False)
