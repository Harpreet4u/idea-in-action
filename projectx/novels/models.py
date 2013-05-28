from django.db import models
from django.contrib.auth.models import User

class Tags(models.Model):
    tag = models.CharField(max_length=50,blank=True, null=True)

    @classmethod
    def create(cls, **kwargs):
        obj=Tags(**kwargs)
        obj.save()
        return obj

class Novel(models.Model):
    
    title           = models.TextField(null=True, blank=True)
    description     = models.TextField(null=True, blank=True)
    content         = models.TextField(null=True, blank=True)
    descrip_tags    = models.ManyToManyField(Tags, blank=True, null=True)
    author          = models.ForeignKey(User, blank=False, null = False)
    #view flag : 'A' for All, 'S' for specific, 'N for none
    viewflag        = models.CharField(max_length=1, blank=False, null=False)
    start_date      = models.DateTimeField(null=True, blank=True)
    update_date     = models.DateTimeField(null=True, blank=True) 
   
    @classmethod
    def create(cls, **kwargs):
        obj=Novel(**kwargs)
        obj.save()
        return obj
    
    def modify(self, **kwargs):
        for key in kwargs:
            self.__setattr__(key,kwargs[key])
        self.save()

class Comments(models.Model):
    comment       = models.TextField(null=True, blank=True)
    user          = models.ForeignKey(User, blank=False, null = False)
    novel         = models.ForeignKey(Novel, blank=False, null = False)
    comment_date  = models.DateTimeField(null=True, blank=True)

    @classmethod
    def create(cls, **kwargs):
        obj=Comments(**kwargs)
        obj.save()
        return obj

class Extendcontent(models.Model):
    novel        = models.ForeignKey(Novel, blank=False, null = False)
    newcontent   = models.TextField(null=True, blank=True)
    contributor  = models.ForeignKey(User, blank=False, null = False) 
    contrib_date = models.DateTimeField(null=True, blank=True)

    @classmethod
    def create(cls, **kwargs):
        obj=Extendcontent(**kwargs)
        obj.save()
        return obj


