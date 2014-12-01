from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(initial="Upit sa liber.hr")
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)