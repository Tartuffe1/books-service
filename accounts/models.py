from django.db import models
from django.contrib.auth.models import User  
from django.utils.translation import ugettext as _  
from userena.models import UserenaBaseProfile  

from django.core.mail import send_mail
  
class MyCustomProfile(UserenaBaseProfile):
     """The Userena User profile"""
     user = models.OneToOneField(User,
         unique=True,
         verbose_name=_('user'),
         related_name='my_profile')
     bio = models.CharField(max_length=1000,default="",blank=True)
     # Make this field not editable because it controls access to uid from legacy db
     my_legacy_user_object = models.SmallIntegerField(null=True,editable=False,unique=True)

     def __unicode__(self):
         return self.bio
