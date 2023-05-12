from django.db import models
from conductor.models import Driver
# Create your models here.

class Vehicle(models.Model):
    modelo = models.CharField('modelo', max_length=8, null=False)
    placa = models.CharField('placa',max_length=7, unique=True, null=False)
    capacidad = models.CharField('capacidad', max_length=7, unique=False, null=True)
    conductor_id = models.ForeignKey(Driver, related_name='conductor_id', on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return self.model
    

    