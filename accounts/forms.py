# encoding: utf-8

from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfile

CATEGORY_CHOICES = (
    ('Zagrebačka', 'Zagrebačka županija'),
    ('Krapinsko-Zagorska', 'Krapinsko-zagorska županija'),
    ('Sisačko-moslavačka', 'Sisačko-moslavačka županija'),
    ('Karlovačka', 'Karlovačka županija'),
    ('Varaždinska', 'Varaždinska županija'),
    ('Koprivničko-križevačka', 'Koprivničko-križevačka županija'),
    ('Bjelovarsko-bilogorska', 'Bjelovarsko-bilogorska županija'),
    ('Međimurska', 'Međimurska županija'),
    ('Grad Zagreb', 'Grad Zagreb'),
    ('Primorsko-goranska', 'Primorsko-goranska županija'),
    ('Ličko-senjska', 'Ličko-senjska županija'),
    ('Istarska', 'Istarska županija'),
    ('Virovitičko-podravska', 'Virovitičko-podravska županija'),
    ('Požeško-slavonska', 'Požeško-slavonska županija'),
    ('Brodsko-posavska', 'Brodsko-posavska županija'),
    ('Osječko-baranjska', 'Osječko-baranjska županija'),
    ('Vukovarsko-srijemska', 'Vukovarsko-srijemska županija'),
    ('Zadarska', 'Zadarska županija'),
    ('Šibensko-kninska', 'Šibensko-kninska županija'),
    ('Splitsko-dalmatinska', 'Splitsko-dalmatinska županija'),
    ('Dubrovačko-neretvanska', 'Dubrovačko-neretvanska županija'),
)
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    # Zelim da email polje bude obvezno.
    email=forms.CharField(max_length=75, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    zupanija=forms.ChoiceField(widget=forms.Select(), choices = CATEGORY_CHOICES)
    
    class Meta:
        model = UserProfile
        fields = ('mobitel', 'zupanija')
