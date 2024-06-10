from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import GrupoMusical
from .models import Author


# admin.site.register(GrupoMusical)


class GrupoMusicalAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('title', 'author', 'created', 'modified')
    date_hierarchy = 'created'


admin.site.register(GrupoMusical, GrupoMusicalAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name' , 'last_name')


admin.site.register(Author, AuthorAdmin)
