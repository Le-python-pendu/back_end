from django.db import models

# Create your models here.

class dictionnaire_t(models.Model):
    word= models.TextField()
    classification = models.TextField()
    definition = models.TextField()
    url_image = models.URLField(max_length=50, default=None)
    frequence = models.IntegerField(default=None)


class dictionnaire_t1(models.Model):
    word= models.CharField(max_length=30)
    classification = models.CharField(max_length=10)
    definition = models.CharField(max_length=100)
    url_image = models.URLField(max_length=50, default=None)
    frequence = models.IntegerField(default=None)
