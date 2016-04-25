from django.conf.urls import patterns, url

from webtool import views

urlpatterns = patterns('',
    # ex: /webtool/
    url(r'^$', views.index, name='index'),
    # ex: /webtool/3/
    url(r'^(?P<room>\d+)/$', views.list, name='list'),
    # ex: /webtool/3/5/
    url(r'^(?P<room>\d+)/(?P<source>\d+)/$', views.set, name='set'),
)

