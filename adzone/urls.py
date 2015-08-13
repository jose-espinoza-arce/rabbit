from django.conf.urls import url
import adzone.mptt_urls as mptt_urls

from adzone.views import ad_view, ListBannersView#, DetailBannerView


urlpatterns = [
    #url(r'^ad/(?P<slug>[-\w]+)$', DetailBannerView.as_view(), name='banner_ad_view'),
    url(r'^$', ListBannersView.as_view(), name='banner_list'),
    url(r'^view/(?P<pk>[\d]+)/$', ad_view, name='ad_view'),
    url(r'^categorias/(?P<path>.*)',
        mptt_urls.view(model='adzone.models.AdCategory',
                       model_object='adzone.models.AdBase',
                       view='adzone.views.ListBannersView',
                       view_object='adzone.views.DetailBannerView',
                       slug_field='slug',
                       ),
        name='ad_categories'
        ),
]
