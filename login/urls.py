from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'login.views.auth'),
    url(r'^api/*$', 'login.views.apiauth'),
    url(r'^redirect/(?P<redirect_url>.*)', 'login.views.auth')
]
