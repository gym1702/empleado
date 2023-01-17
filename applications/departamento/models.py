from django.db import models

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre corto', max_length=20, blank=True, null=True, unique=True)
    active = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name_plural = 'Departamentos'
        ordering = ['name']

    def __str__(self):
        return self.name

    

    
