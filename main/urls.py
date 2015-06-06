from django.conf.urls import patterns, url

from main.views import stats_yearly, import_data, import_data_report, \
    import_total, import_partial
from views import index, manual, docs, stats


urlpatterns = patterns('',
    url(r'^$',index),
    url(r'^manual/$',manual),
    url(r'^documentacion/$',docs),
    url(r'^estadisticas/$',stats),
    url(r'^estadisticas/anual/$',stats_yearly),
    url(r'^importar/$',import_data),
    url(r'^importar/total/$',import_total),
    url(r'^importar/parcial/$',import_partial),
    url(r'^importar/reporte/$',import_data_report),
)
