# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save

class UserProfile(models.Model):
    CATEGORY_CHOICES = (
        ('zagrebacka', 'Zagrebaèka županija'),
        ('krapinsko-zagorska', 'Krapinsko-zagorska županija'),
        ('sisacko-moslavacka', 'Sisaèko-moslavaèka županija'),
        ('karlovacka', 'Karlovaèka županija'),
        ('varazdinska', 'Varaždinska županija'),
        ('koprivnicko-krizevacka', 'Koprivnièko-križevaèka županija'),
        ('bjelovarsko-bilogorska', 'Bjelovarsko-bilogorska županija'),
        ('medjimurska', 'Meðimurska županija'),
        ('grad-zagreb', 'Grad Zagreb'),
        ('primorsko-goranska', 'Primorsko-goranska županija'),
        ('licko-senjska', 'Lièko-senjska županija'),
        ('istarska', 'Istarska županija'),
        ('viroviticko-podravska', 'Virovitièko-podravska županija'),
        ('pozesko-slavonska', 'Požeško-slavonska županija'),
        ('brodsko-posavska', 'Brodsko-posavska županija'),
        ('osjecko-baranjska', 'Osjeèko-baranjska županija'),
        ('vukovarsko-srijemska', 'Vukovarsko-srijemska županija'),
        ('zadarska', 'Zadarska županija'),
        ('sibensko-kninska', 'Šibensko-kninska županija'),
        ('splitsko-dalmatinska', 'Splitsko-dalmatinska županija'),
        ('dubrovacko-neretvanska', 'Dubrovaèko-neretvanska županija'),
    )
    user = models.OneToOneField(User)

    zupanija = models.CharField(max_length=40, choices=CATEGORY_CHOICES, default='zagrebacka')
    mobitel = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.user.username
        
