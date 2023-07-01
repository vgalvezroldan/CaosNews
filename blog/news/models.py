from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.

# MODELO CATEGORIA

class Category (models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name'] 

    def __str__(self):
        return self.name


# MODELO DE ETIQUETAS

class Tag (models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ['name'] 

    def __str__(self):
        return self.name

# MODELO DE AUTOR = USUARIOS REGISTRADOS EN LA APP (IMPORTANDO TABLA USUARIOS)

# MODELO DE LOS POSTS

class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Titulo')
    excerpt = models.TextField(verbose_name='Bajada')
    #content = models.TextField(verbose_name='Contenido')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='posts',null=True, blank=True, verbose_name='Imagen')
    published = models.BooleanField(default=False, verbose_name='Publicado')

    # Campos con relaciones

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='get_posts' , verbose_name='Categoria')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='get_posts' , verbose_name='Autor')
    tags = models.ManyToManyField(Tag, verbose_name='Etiquetas')

    created = models.DateTimeField(default=timezone.now, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-created'] 

    def __str__(self):
        return self.title
    
#############################################

# Modelo About

class About(models.Model):
    description = models.CharField(max_length=350, verbose_name='Descripcion')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Acerca de'
        verbose_name_plural = 'Acerca de Nosotros'
        ordering = ['-created'] 

    def __str__(self):
        return self.description
        
# MODELO LINK = Redes Sociales

class Link(models.Model):
    key = models.CharField(max_length=100, verbose_name='Key Link')
    name = models.CharField(max_length=120,verbose_name='Red Social')
    url = models.URLField(max_length=350, blank=True, null=True ,verbose_name='Enlace')
    icon = models.CharField(max_length=100,verbose_name='Icono',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'
        ordering = ['name'] 

    def __str__(self):
        return self.name