# Create your views here.
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.utils import simplejson
from django.shortcuts import render_to_response ,render,redirect
from django.contrib.auth.decorators import login_required

def render_createnovel(request):
    return render_to_response('createnovels.html',{'user_id':1},context_instance=RequestContext(request))



