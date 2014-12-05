# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save

class UserProfile(models.Model):
    
    user = models.OneToOneField(User)

    zupanija = models.CharField(max_length=40,blank=True)
    mobitel = models.CharField(max_length=20,blank=True)
    
    def __unicode__(self):
        return self.user.username
        
