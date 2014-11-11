from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

PROFILE_PERMISSIONS = (
            ('view_profile', 'Can view profile'),
            ('change_profile', 'Change Profile'),
            ('delete_profile', 'Delete Profile'),
)

class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
    favourite_snack = models.CharField(_('favourite snack'),
                                       max_length=5)
                                       
    class Meta:
       permissions = PROFILE_PERMISSIONS