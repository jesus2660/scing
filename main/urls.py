from django.conf.urls import patterns, url

from main.views import index


urlpatterns = patterns('',
    url(r'^$',index)
)
