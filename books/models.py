from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    docfile = models.FileField(upload_to='images', default='images/default.jpg')
    
    # Povezujemo knjigu sa korisnikom (userom) koji ju je uploadao:
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title
