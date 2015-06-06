from django.conf.urls import patterns, include, url
from .views import index, consulter, logout, register, addrecette

urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       url(r'^consulter/$', consulter, name='consulter'),
                       url(r'^ajouter_recette/$', addrecette, name='addRecette'),

                       # USER PART
                       url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'recettes/login.html'}),
                       url(r'^logout/$', logout, name='logout'),

                       url(r'^logged_in/$', 'recettes.views.logged_in'),
                       url(r'^register/$', register, name='register'),
                    )
