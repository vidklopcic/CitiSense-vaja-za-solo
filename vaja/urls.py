from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'vaja.views.index'),
    url(r'^put/(?P<token>[^/]+)/(?P<measurements>[^/]+)/(?P<reading>[^/]+)', 'vaja.views.put_value'),
    url(r'^(?P<name>.*$)', 'vaja.views.measurements'),
]
