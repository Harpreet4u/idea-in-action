from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
import os


urlpatterns = patterns('',
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':os.getcwd()+'/novels/static'}),
    url(r'create/',              'novels.views.render_createnovel'),
    url(r'^editor/(?P<path>.*)$','django.views.static.serve',{'document_root':os.getcwd()+'/novels/editor'}),
)
