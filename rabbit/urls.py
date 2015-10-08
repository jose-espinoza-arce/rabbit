"""rabbit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin


from django.conf.urls.static import static
from django.conf import settings

from jet import urls as jet_urls
from jet.dashboard import urls as dash_urls


#admin.site = AdminSitePlus()
#admin.autodiscover()


urlpatterns = [
    #url(r'^grappelli/', include('grappelli.urls')),
    url(r'^jet/', include(jet_urls, 'jet')),
    url(r'^jet/dashboard/', include(dash_urls, 'jet-dashboard')),
    url(r'^intranetRoof/', include(admin.site.urls)),
    #url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^feedback/', include('feedback_form.urls')),
    url(r'^dynamic_forms/',
        include('dynamic_forms.urls', namespace='dynamic_forms')),
    url(r'^likes/', include('likes.urls')),
]

if settings.DEBUG:
    # Server statics and uploaded media
    urlpatterns += [url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})]

#Added at the end so 'path' don't interfere with media, admin or any other urls
urlpatterns += [
    url(r'^', include('content.urls', namespace='content')),
]