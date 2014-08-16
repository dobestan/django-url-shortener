from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# Custom View
from links.views import LinkRedirect

urlpatterns = patterns('',
    url(r'^api/', include('API.urls', namespace="API")),
    url(r'^(?P<shorten>[0-9a-zA-Z]+)/$', LinkRedirect.as_view(), name="link-redirect"),
)
