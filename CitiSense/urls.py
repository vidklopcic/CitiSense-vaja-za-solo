from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('vaja.urls')),
    url(r'^measurements/', include('vaja.urls')),
    url(r'^api/', include('vaja.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include('login.urls')),
]