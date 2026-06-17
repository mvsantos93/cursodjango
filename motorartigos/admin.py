from django.contrib import admin
from .models import Autor, EixoTecnologia

# Register your models here.

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'biografia', 'email')
    search_fields = ('nome', 'email')

admin.site.register(Autor, AutorAdmin)