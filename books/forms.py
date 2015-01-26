# encoding: utf-8

from django import forms
from models import Book

CATEGORY_CHOICES = (
    ('expert', 'Stručna literatura'),
    ('classic', 'Književnost i beletristika'),
    ('antiquarian', 'Antikvarne knjige'),
    ('foreign', 'Strana literatura'),
    ('encyclopedias', 'Enciklopedije i priručnici'),
    ('periodicals', 'Periodika'),
    ('comics', 'Stripovi'),
    ('ostala', 'Ostala literatura'),
)

class BookForm(forms.ModelForm):
   class Meta:
      model=Book
      exclude = ['user','pub_date']
      
# Klasu ispod uveo sam radi prijevoda svih polja na hrvatski, nisam mogao to riješiti kao za add_book
class BookEditForm(BookForm):
    title = forms.CharField(label="Naslov")
    category = forms.ChoiceField(widget=forms.Select(), choices = CATEGORY_CHOICES, label="Kategorija")
    description = forms.CharField(widget = forms.Textarea, label="Opis")
    price= forms.IntegerField(label="Cijena")
    docfile = forms.FileField(label="Slika")