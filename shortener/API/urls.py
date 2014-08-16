from django.conf.urls import patterns, url
from API import views

urlpatterns = patterns('',
        url(r'^links/$', views.LinkList.as_view(), name="link-list"),
)
