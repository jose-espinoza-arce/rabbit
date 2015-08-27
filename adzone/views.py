# -*- coding: utf-8 -*-

# © Copyright 2009 Andre Engelbrecht. All Rights Reserved.
# This script is licensed under the BSD Open Source Licence
# Please see the text file LICENCE for more information
# If this script is distributed, it must be accompanied by the Licence

from django.db.models import Count
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView

from django.contrib import messages
from django.utils import timezone
import json

from adzone.models import AdBase, AdClick, AdBase, AdImpression, AdPhoneView
from django.shortcuts import get_object_or_404, redirect

from taggit.models import Tag

from adzone.forms import AdSearchForm


class AdListView(ListView):
    model = AdBase
    paginate_by = 10

    def get_context_data(self, **kwargs):
        ctx = super(AdListView, self).get_context_data(**kwargs)
        slugs = self.request.path.split('/')
        q = ''

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
            elif 'slugs' in kwargs.keys():
                self.queryset = queryset.filter(tags__slug__in=kwargs.pop('slugs')).distinct()
            else:
                print 'adlisview.get.else'
                return redirect('adzone:ad_list')

        return super(AdListView, self).get(request, *args, **kwargs)


class AdDetailView(DetailView):
    model = AdBase

    def get_context_data(self, **kwargs):
        ctx = super(AdDetailView, self).get_context_data(**kwargs)
        ctx['search_form'] = AdSearchForm()
        return ctx

    def get(self, request, *args, **kwargs):
        request.META["CSRF_COOKIE_USED"] = True

        if not kwargs['instance']:
            return redirect('adzone:ad_list')

        try:
            impression = AdImpression(
                ad=self.get_object(),
                impression_date=timezone.now(),
                source_ip=request.META.get('REMOTE_ADDR'),
            )
            impression.save()
        except:
            pass

        return super(AdDetailView, self).get(request, *args, **kwargs)


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
