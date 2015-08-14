from django.conf.urls import url
import adzone.mptt_urls as mptt_urls

from adzone.views import ad_view, ad_phone_view, AdListView#, DetailBannerView


urlpatterns = [
    #url(r'^ad/(?P<slug>[-\w]+)$', DetailBannerView.as_view(), name='banner_ad_view'),
    url(r'^$', AdListView.as_view(), name='ad_list'),
    url(r'^view/(?P<pk>[\d]+)/$', ad_view, name='ad_view'),
    url(r'^phone/', ad_phone_view, name='ad_phone_view'),
    url(r'^categorias/(?P<path>.*)',
        mptt_urls.view(model='adzone.models.AdCategory',
                       model_object='adzone.models.AdBase',
                       view='adzone.views.AdListView',
                       view_object='adzone.views.AdDetailView',
                       slug_field='slug',
                       ),
        name='ad_categories'
        ),
]
