# encoding: utf-8

from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfile

CATEGORY_CHOICES = (
    ('zagrebacka', 'Zagrebačka županija'),
    ('krapinsko-zagorska', 'Krapinsko-zagorska županija'),
    ('sisacko-moslavacka', 'Sisačko-moslavačka županija'),
    ('karlovacka', 'Karlovačka županija'),
    ('varazdinska', 'Varaždinska županija'),
    ('koprivnicko-krizevacka', 'Koprivničko-križevačka županija'),
    ('bjelovarsko-bilogorska', 'Bjelovarsko-bilogorska županija'),
    ('medjimurska', 'Međimurska županija'),
    ('grad-zagreb', 'Grad Zagreb'),
    ('primorsko-goranska', 'Primorsko-goranska županija'),
    ('licko-senjska', 'Ličko-senjska županija'),
    ('istarska', 'Istarska županija'),
    ('viroviticko-podravska', 'Virovitičko-podravska županija'),
    ('pozesko-slavonska', 'Požeško-slavonska županija'),
    ('brodsko-posavska', 'Brodsko-posavska županija'),
    ('osjecko-baranjska', 'Osječko-baranjska županija'),
    ('vukovarsko-srijemska', 'Vukovarsko-srijemska županija'),
    ('zadarska', 'Zadarska županija'),
    ('sibensko-kninska', 'Šibensko-kninska županija'),
    ('splitsko-dalmatinska', 'Splitsko-dalmatinska županija'),
    ('dubrovacko-neretvanska', 'Dubrovačko-neretvanska županija'),
)
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    zupanija=forms.ChoiceField(widget=forms.Select(), choices = CATEGORY_CHOICES)
    
    class Meta:
        model = UserProfile
        fields = ('mobitel', 'zupanija')
