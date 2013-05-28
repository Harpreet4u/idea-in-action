from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
import os
import novels

urlpatterns = patterns('',
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':os.getcwd()+'/static'}),
    url(r'^accounts/', include('registration.urls')),
    url(r'novels/',include('novels.urls')),
)

