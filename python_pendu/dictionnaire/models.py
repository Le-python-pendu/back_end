from django.db import models

# Create your models here.

class dictionnaire(models.Model):
    word= models.CharField(max_length=30)
    classification = models.CharField(max_length=10)
    definition = models.CharField(max_length=100)
    url_image = models.URLField(max_length=50, default=None)
    frequence = models.IntegerField(default=None)
