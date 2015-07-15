from django.db import models
from location_field.models.plain import PlainLocationField

# Create your models here.
class Departamento(models.Model):
    nombre = models.TextField(max_length=100)
    descripcion = models.TextField(max_length=300)
    imagen = models.TextField(max_length=100)
    circuitos = models.TextField(max_length=100, blank= True)
    
    def __str__(self):
        return self.nombre
    
    @models.permalink
    def get_absolute_url(self):
        return ('departamento-detail', (self.pk, ))
    
class Categoria(models.Model):
    categoria = models.TextField(max_length=100)
    descripcion = models.TextField(max_length=150, blank= True)
    departamento = models.ForeignKey(Departamento)
    
    def __str__(self):
        return self.categoria
    
    @models.permalink
    def get_absolute_url(self):
        return ('categoria-detail', (self.pk, ))
   
class RecursoNatural(models.Model):
    nombre = models.TextField(max_length=100)
    descripcion = models.TextField(max_length=300)
    imagen = models.TextField(max_length=100)
    departamento = models.ForeignKey(Departamento)
    categoria = models.ForeignKey(Categoria)
    
    def __str__(self):
        return self.nombre
    
    @models.permalink
    def get_absolute_url(self):
        return ('recursonatural-detail', (self.pk, ))
    
class RecursoCultural(models.Model):
    nombre = models.TextField(max_length=100)
    historia = models.TextField(max_length=300)
    direccion = models.TextField(max_length=100)
    imagen = models.TextField(max_length=100)
    punto = PlainLocationField(based_fields=[nombre],
                               zoom=8,
                               verbose_name='Lugar:',
                               blank=True,
                               null=True,
                               )
    departamento = models.ForeignKey(Departamento)
    categoria = models.ForeignKey(Categoria)
    
    def __str__(self):
        return self.nombre

class Coordenada(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()
    recurso_nat = models.ForeignKey(RecursoNatural, blank=True)
    resurso_cult =  models.ForeignKey(RecursoCultural, blank=True)
    departamento = models.OneToOneField(Departamento)
    