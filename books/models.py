# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
# osigurat cemo jedinstveno ime za uploadana slike:
from time import time
from datetime import datetime 

# Zelim dobiti ne predugo, ali dovoljno unikatno ime"
def get_file_path(instance, filename):
    return "images/%s.%s" %(str(time()).replace(".","_"), filename.split('.').pop())

class Book(models.Model):
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
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=15, choices = CATEGORY_CHOICES)
    description = models.TextField(max_length=1000, blank=True)
    docfile = models.FileField(upload_to=get_file_path,
                        null=True,
                        blank=True,
                        default='images/default.jpg',
                        )
    #vrijeme stavljanja oglasa samo ce se upisati:
    pub_date=models.DateTimeField(default=datetime.now, blank=True)
    
    # Povezujemo knjigu sa korisnikom (userom) koji ju je uploadao:
    user = models.ForeignKey(User)
    
    price= models.IntegerField()
    
    def __unicode__(self):
        return self.title
