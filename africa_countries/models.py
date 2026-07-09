from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils import timezone

class AfricaCountry(models.Model):
    name = models.CharField(max_length=100, unique=True)
    capital = models.CharField(max_length=100)
    population = models.PositiveIntegerField()
    area = models.FloatField(help_text="Area in square kilometers")
    official_language = models.CharField(max_length=100)
    currency = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    region = models.CharField(max_length=100, choices=[
        ('NORTH', 'Northern Africa'),
        ('WEST', 'Western Africa'),
        ('CENT', 'Central Africa'),
        ('EAST', 'Eastern Africa'),
        ('SOUTH', 'Southern Africa'),
    ])
    class Meta:
        verbose_name = "African Country"
        verbose_name_plural = "African Countries"
        ordering = ['name']
    
    def __str__(self):
        return self.name