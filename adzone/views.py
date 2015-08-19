# -*- coding: utf-8 -*-

# © Copyright 2009 Andre Engelbrecht. All Rights Reserved.
# This script is licensed under the BSD Open Source Licence
# Please see the text file LICENCE for more information
# If this script is distributed, it must be accompanied by the Licence


from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView
from django.utils import timezone

from adzone.models import AdBase, AdClick, AdBase, AdImpression, AdPhoneView
from django.shortcuts import get_object_or_404, redirect




class AdListView(ListView):
    model = AdBase
    paginate_by = 5

    def get_queryset(self):
        qs = super(AdListView, self).get_queryset()
        qs = qs.filter(start_showing__lte=timezone.now(),
                       stop_showing__gte=timezone.now(),).order_by('-pk')

        return qs

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if 'instance' and 'path' in kwargs.keys():
            if kwargs['instance']:
                descendants = kwargs['instance'].get_descendants(include_self=True)
                self.queryset = queryset.filter(category__in=descendants)
            else:
                return redirect('adzone:ad_list')

        return super(AdListView, self).get(request, *args, **kwargs)


class AdDetailView(DetailView):
    model = AdBase

    def get(self, request, *args, **kwargs):

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


#def get_ads(request):
#    if request


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
