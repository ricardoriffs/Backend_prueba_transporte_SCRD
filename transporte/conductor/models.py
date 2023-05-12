from django.db import models

# Create your models here.

class Driver(models.Model):
    identificacion = models.CharField('identification', max_length=15, unique=True, null=False)
    nombre = models.CharField('nombre',max_length=20, unique=False, null=False)
    apellido = models.CharField('apellido',max_length=20, unique=False, null= True)
    telefono = models. CharField('telefono', max_length=10, unique=False, null=False)
    direccion = models.CharField('direccion',max_length=50, null=True)


    def __str__(self):
        return f'Conductor {self.name} con identificación {self.identification}'
    

    