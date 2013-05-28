from django.db import models
from django.contrib.auth.models import User
import datetime
import hashlib
import random
import re
import Image
import subprocess
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db import transaction
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.mail import EmailMultiAlternatives
attrs_dict = {'class': 'required'}

site = 'www.supreetpal.in'
SHA1_RE = re.compile('^[a-f0-9]{40}$')

class RegisterationForm(forms.Form):
    username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                widget=forms.TextInput(attrs=attrs_dict),
                                label=_("Username"),
                                error_messages={
                                  'invalid': _("This value may contain only \
                                  letters, numbers and @/./+/-/_ characters.")})
    email     = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                maxlength=75)),label=_("E-mail"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict,
                                render_value=False),label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict,
                                render_value=False),label=_("Password (again)"))

    def clean_username(self):
        existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError(_("A user with that username already exists."))
        else:
            return self.cleaned_data['username']

    def clean_email(self):
        existing = User.objects.filter(email__iexact=self.cleaned_data['email'])
        if existing.exists():
            raise forms.ValidationError(_("A user with that email already exists."))
        else:
            return self.cleaned_data['email']

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data

    def save(self):
        new_user = uProfile()
        new_user.create_inactive_user(
                        username=self.cleaned_data['username'],
                        password=self.cleaned_data['password1'],
                        email=self.cleaned_data['email'],
                        )
        return new_user
 
class uProfile(models.Model):
    
    user      = models.ForeignKey(User, unique=True, verbose_name=_('user'))
    rating    = models.DecimalField(max_digits=3,decimal_places=2,blank=False)
    city      = models.CharField(max_length = 50)
    address   = models.TextField()
    contact_no= models.IntegerField(max_length=11,null=True,blank=True)    

    def create_inactive_user(self,username,password,email):
      print "Created    ///"
      new_user = User.objects.create_user(username,email,password)
      new_user.save()
      new_user_profile = uProfile()
      new_user_profile.user = new_user
      new_user_profile.rating = 2.5
      new_user_profile.save()
      username = new_user.username
      html = '<a href ='+site+'>'+site +'</a>'
      if new_user.email != None:
        msg = EmailMultiAlternatives('Fucking Registered', ("%s Dude ,.. you are lucky to be fucked by us... Follow Us")%(username), 'kweqen.info@gmail.com', [email,])
        msg.attach_alternative(html, "text/html")
        msg.send()


