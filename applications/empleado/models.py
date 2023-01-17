from django.db import models
from ckeditor.fields import RichTextField

from applications.departamento.models import Departamento



class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name_plural = 'Habilidades'
        ordering = ['habilidad']

    def __str__(self):
        return self.habilidad


class Empleado(models.Model):
    job = (
        ('Contador', 'Contador'),
        ('Administrador', 'Administrador'),
        ('Economista', 'Economista'),
        ('Otro', 'Otro'),
    )

    first_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    full_name = models.CharField('Nombre completo', max_length=100, blank=True, null=True)
    job = models.CharField('Puesto', choices=job, max_length=30)
    department = models.ForeignKey(Departamento, on_delete=models.CASCADE) #realacion de uno a muchos
    habilidades = models.ManyToManyField(Habilidades) #Relacion de muchos a muchos
    hoja_vida = RichTextField()
    image = models.ImageField('Imagen', upload_to='empleados', default='empleados/logo_bueno.png', blank=True, null=True)
    active = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name_plural = 'Empleados'
        ordering = ['first_name']
    
    # def nombre_completo(self):
    #     return self.first_name +' '+ self.last_name

    def __str__(self):
        return self.first_name + ' ' + self.last_name