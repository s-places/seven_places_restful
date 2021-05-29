"""Django models"""
from django.db import models


class Continent(models.Model):
    """Data structure for continent of the world"""
    objects = models.Manager()
    
    class Meta:
        verbose_name = "Continent"

    def __str__(self):
        return self.name
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True)
    place = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30, blank=True)
    population = models.PositiveIntegerField(blank=True)
    overview = models.TextField(blank=True)
    languages = models.CharField(max_length=40, blank=True)
    first_image = models.ImageField(blank=True)
    second_image = models.ImageField(blank=True)
    third_image = models.ImageField(blank=True)