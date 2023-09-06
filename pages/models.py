from django.db import models
from ckeditor.fields import RichTextField # PARA EL CKEDITOR

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=50, verbose_name='Título')
    # content = models.TextField(verbose_name='Contenido')
    content = RichTextField(verbose_name='Contenido') # DJANGO-CKEDITOR => AÑADIR EN SETTING LA CONFIGUARACION Y ADICION DE FUNCIONES ADICIONALES
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    
    
    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['created']
    
    def __str__(self):
        return self.title
    
        