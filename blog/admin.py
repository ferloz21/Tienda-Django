from django.contrib import admin
from .models import categoria, Post

# Register your models here.


class categoriaAdmin(admin.ModelAdmin):
    readonly_fields=('create','update')


class PostAdmin(admin.ModelAdmin):
    readonly_fields=('create','update')



admin.site.register(categoria, categoriaAdmin)

admin.site.register(Post, PostAdmin)


