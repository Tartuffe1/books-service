from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    docfile = models.FileField(upload_to='images', default='images/default.jpg')
    
    # Povezujemo knjigu sa korisnikom (userom) koji ju je uploadao:
    user = models.ForeignKey('accounts.MyProfile')
    
    def __unicode__(self):
        return self.title
