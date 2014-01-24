from django.conf.urls import patterns, url

from events import views

# urlpatterns = patterns('',
    # url(r'^$', views.index, name='index')
    # url(r'^', views.index, name='index')
# )

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/?$', views.about, name='about'),
    url(r'^press/?$', views.press, name='press'),
    url(r'^(?P<slug>[-_\w]+)/?$', views.DetailView.as_view(), name='detail'),
)
