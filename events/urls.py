from django.conf.urls import patterns, url
from django.shortcuts import redirect

from events import views

sitemaps = {
    'events': views.EventsSitemap,
    'static': views.StaticViewSitemap,
}

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^press/', views.press, name='press'),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^(?P<slug>[-_\w]+)/$', views.DetailView.as_view(), name='events'),
)
