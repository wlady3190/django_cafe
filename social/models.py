from django.db import models

# Create your models here.

class Social(models.Model):
    key = models.SlugField(verbose_name='Nombre clave', max_length=50, unique=True)#CREANDO CLAVES UNICAS, PERMITE -,_  y alfanumericos
    name=models.CharField(max_length=50, verbose_name='Red Social')
    url = models.URLField(verbose_name='Enlace', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    
    class Meta:
        verbose_name = 'Red social'
        verbose_name_plural = 'Redes sociales'
        ordering = ['name']
    
    def __str__(self):
        return self.name