# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save

class UserProfile(models.Model):
    CATEGORY_CHOICES = (
        ('zagrebacka', 'Zagreba�ka �upanija'),
        ('krapinsko-zagorska', 'Krapinsko-zagorska �upanija'),
        ('sisacko-moslavacka', 'Sisa�ko-moslava�ka �upanija'),
        ('karlovacka', 'Karlova�ka �upanija'),
        ('varazdinska', 'Vara�dinska �upanija'),
        ('koprivnicko-krizevacka', 'Koprivni�ko-kri�eva�ka �upanija'),
        ('bjelovarsko-bilogorska', 'Bjelovarsko-bilogorska �upanija'),
        ('medjimurska', 'Me�imurska �upanija'),
        ('grad-zagreb', 'Grad Zagreb'),
        ('primorsko-goranska', 'Primorsko-goranska �upanija'),
        ('licko-senjska', 'Li�ko-senjska �upanija'),
        ('istarska', 'Istarska �upanija'),
        ('viroviticko-podravska', 'Viroviti�ko-podravska �upanija'),
        ('pozesko-slavonska', 'Po�e�ko-slavonska �upanija'),
        ('brodsko-posavska', 'Brodsko-posavska �upanija'),
        ('osjecko-baranjska', 'Osje�ko-baranjska �upanija'),
        ('vukovarsko-srijemska', 'Vukovarsko-srijemska �upanija'),
        ('zadarska', 'Zadarska �upanija'),
        ('sibensko-kninska', '�ibensko-kninska �upanija'),
        ('splitsko-dalmatinska', 'Splitsko-dalmatinska �upanija'),
        ('dubrovacko-neretvanska', 'Dubrova�ko-neretvanska �upanija'),
    )
    user = models.OneToOneField(User)

    zupanija = models.CharField(max_length=40, choices=CATEGORY_CHOICES, default='zagrebacka')
    mobitel = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.user.username
        
