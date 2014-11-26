# encoding: utf-8
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
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
    email = forms.EmailField(required=True)
    mobitel=forms.CharField(max_length=20, required=False)
    zupanija=forms.ChoiceField(choices = CATEGORY_CHOICES, required=False)
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "mobitel", "zupanija")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.mobitel = self.cleaned_data["mobitel"]
        user.zupanija = self.cleaned_data["zupanija"]
        if commit:
            user.save()
        return user

attrs_dict = {'class': 'required'}

class ChangeEmailForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=75)),
                             label="New email")

    def __init__(self, user, *args, **kwargs):
        """
        The current ``user`` is needed for initialisation of this form so
        that we can check if the email address is still free and not always
        returning ``True`` for this query because it's the users own e-mail
        address.

        """
        super(ChangeEmailForm, self).__init__(*args, **kwargs)
        if not isinstance(user, get_user_model()):
            raise TypeError("user must be an instance of %s" % get_user_model().__name__)
        else: self.user = user

    def clean_email(self):
        """ Validate that the email is not already registered with another user """
        if self.cleaned_data['email'].lower() == self.user.email:
            raise forms.ValidationError(_(u'You\'re already known under this email.'))
        if get_user_model().objects.filter(email__iexact=self.cleaned_data['email']).exclude(email__iexact=self.user.email):
            raise forms.ValidationError(_(u'This email is already in use. Please supply a different email.'))
        return self.cleaned_data['email']

    def save(self):
        """
        Save method calls :func:`user.change_email()` method which sends out an
        email with an verification key to verify and with it enable this new
        email address.

        """
        return self.user.userena_signup.change_email(self.cleaned_data['email'])