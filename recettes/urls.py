from django.conf.urls import patterns, include, url
from .views import index, consulter, login, auth_view, logout, loggedin, invalid_login

urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       url(r'^consulter/$', consulter, name='consulter'),

                       # USER PART
                       url(r'^login/$', login, name='login'),
                       url(r'^auth/$', auth_view, name='auth_view'),
                       url(r'^logout/$', logout, name='logout'),
                       url(r'^loggedin/$', loggedin, name='loggedin'),
                       url(r'^invalid/$', invalid_login, name='invalid_login'),
)
