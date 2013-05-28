from django.contrib import auth
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.context_processors.auth import RequestContext
from django.views.decorators.csrf import csrf_exempt
from registration.models import RegisterationForm

@csrf_exempt
def login_view(request):
    template = '/userpage/'
    username = request.POST.get('username', '')
    print username
    password = request.POST.get('password', '')
    print password
    user = auth.authenticate(username=username, password=password)
    print user
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return render_to_response('index.html',{'user':user,'user_id':user.id})
        
    else:
        # Show an error page
        return render_to_response("/error.html/",{})

def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/Bids/")

@csrf_exempt
def rendering(request,form_class=RegisterationForm):
  form = form_class()
  return render_to_response('index.html',{'form':form})

@csrf_exempt
def render(request):
  return render_to_response('login.html',{})

@csrf_exempt
def register(request,form_class=RegisterationForm):
    if request.method == 'POST':
        print "POSTing"
        form = form_class(request.POST)
        print form
        if form.is_valid():
            print "///////////////////////////////////////////////////////"
            new_user = form.save()
            return render_to_response("userpage.html",{'user':new_user})
    else:
        form = form_class()
    return render_to_response("register.html", {
        'form': form,
    })


