# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    CATEGORY_CHOICES = (
        ('expert', 'Stručna literatura'),
        ('classic', 'Književnost i beletristika'),
        ('antiquarian', 'Antikvarne knjige'),
        ('foreign', 'Strana literatura'),
        ('encyclopedias_and_handbooks', 'Enciklopedije i priručnici'),
        ('periodicals', 'Periodika'),
        ('comics', 'Stripovi'),
        ('ostala', 'Ostala literatura'),
    )
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=15, choices = CATEGORY_CHOICES)
    description = models.TextField(max_length=1000)
    docfile = models.FileField(upload_to='images', default='images/default.jpg')
    
    # Povezujemo knjigu sa korisnikom (userom) koji ju je uploadao:
    user = models.ForeignKey(User)
    
    price= models.IntegerField()
    
    def __unicode__(self):
        return self.title
