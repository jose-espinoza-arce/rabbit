from django.conf.urls import url

from taggit.models import Tag

import adzone.mptt_urls as mptt_urls
from adzone.views import ad_view, ad_phone_view, tag_hint, AdListView


urlpatterns = [
    #url(r'^ad/(?P<slug>[-\w]+)$', DetailBannerView.as_view(), name='banner_ad_view'),
    url(r'^$', AdListView.as_view(), name='ad_list'),
    url(r'^view/(?P<pk>[\d]+)/$', ad_view, name='ad_view'),
    url(r'^phone/', ad_phone_view, name='ad_phone_view'),
    url(r'^taghint/', tag_hint, name='tag_hint'),
    url(r'^search/', mptt_urls.searchview(), name='search'),
    url(r'^categorias/(?P<path>.*)',
        mptt_urls.view(model='adzone.models.AdCategory',
                       model_object='adzone.models.AdBase',
                       view='adzone.views.AdListView',
                       view_object='adzone.views.AdDetailView',
                       slug_field='slug',
                       ),
        name='ad_categories'
        ),
    url(r'^tags/(?P<path>.*)',
        mptt_urls.tagview(tagmodel=Tag,
                          view=AdListView,
                          slug_field='slug'),
        name='tagged_ads'),
]
