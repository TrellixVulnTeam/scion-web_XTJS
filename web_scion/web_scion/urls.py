from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

urlpatterns = patterns('',
    url(r'^$', lambda _: HttpResponseRedirect(reverse('list_isds'))),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ad_manager/', include('ad_manager.urls')),
)
