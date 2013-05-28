from django.conf.urls import patterns, include, url
from registration.views import *
import os
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.conf.urls.defaults import *
from registration import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test1.views.home', name='home'),
    # url(r'^test1/', include('test1.foo.urls')),
    url (r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':os.getcwd()+'/static'}),
    # (r'^accounts/logout/$','django.contrib.auth.views.logout'),
    # (r'^accounts/login/$','django.contrib.auth.views.login', {'template_name':'admin/login.html'}),
    # (r'^accounts/$', 'django.views.generic.simple.redirect_to',{'url':'/'}),
    # (r'^accounts/$', 'django.views.generic.simple.redirect_to',{'url':'/'}),
     #(r'^accounts/profile/$', '')
    (r'^/login/$', login_view),
    (r'^/logout/$', logout_view),
    (r'^/$','registeration.views.rendering'),
    (r'^render/$',render),
    (r'^/register/$', register),
   # (r'^user/$', userpage),
    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

