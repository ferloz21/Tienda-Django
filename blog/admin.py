from django.contrib import admin
from .models import Categoria, Post

# Register your models here.


class categoriaAdmin(admin.ModelAdmin):
    readonly_fields=('create','update')


class PostAdmin(admin.ModelAdmin):
    readonly_fields=('create','update')



admin.site.register(Categoria, categoriaAdmin)

admin.site.register(Post, PostAdmin)


