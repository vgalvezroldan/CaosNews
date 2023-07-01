from django.contrib import admin
from .models import Category, Tag, Post, About, Link
admin.site.site_header = 'Administración de Noticias | Caos News'
admin.site.index_title = 'Panel de Control'
admin.site.site_title = 'Caos News'

# Register your models here.


# Categorias

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'active', 'created') 

admin.site.register(Category, CategoryAdmin)

# Etiquetas

class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'active', 'created') 

admin.site.register(Tag, TagAdmin)
 
# Post

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','category', 'published','author', 'created', 'post_tags',) 
    ordering = ('author', 'created')
    search_fields = ('title','content','author__username','category__name')
    list_filter = ('author','tags',)

    def post_tags(self,obj):
        return ' -'.join([t.name for t in obj.tags.all().order_by('name')])

    post_tags.short_description = 'Etiquetas'

admin.site.register(Post, PostAdmin)

# ABOUT

class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('description', 'created',) 

admin.site.register(About, AboutAdmin)

# REDES SOCIALES

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'key','url','icon')

admin.site.register(Link, LinkAdmin) 


