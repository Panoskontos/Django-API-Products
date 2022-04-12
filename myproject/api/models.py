from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    price = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100,blank=True)
    starring = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
