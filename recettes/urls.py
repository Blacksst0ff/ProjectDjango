from django.conf.urls import patterns, include, url
from .views import index, consulter

urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       url(r'^consulter/$', consulter, name='consulter'),
)
