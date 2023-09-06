from django.db import models
from django.utils.timezone import now # fecha del servidor
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre categoría')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name'] #orden de A a Z
        
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de publicación', default=now) # creando fecha del servidor por default
    image = models.ImageField(verbose_name='Imagen', upload_to='blog')
    author = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name='Autor' )
    categories = models.ManyToManyField(Category, verbose_name='Categorias')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    
    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created']
    
    def __str__(self):
        return self.title
    