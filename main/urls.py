from django.conf.urls import patterns, url

from main.views import stats_yearly
from views import index, manual, docs, stats


urlpatterns = patterns('',
    url(r'^$',index),
    url(r'^manual/$',manual),
    url(r'^documentacion/$',docs),
    url(r'^estadisticas/$',stats),
    url(r'^estadisticas/anual/$',stats_yearly),
)
