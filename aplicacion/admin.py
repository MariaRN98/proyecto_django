from django.contrib import admin
from .models import Categoria, Juego, Mecanica, Usuario, Prestamo
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import UserManager
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Juego)
admin.site.register(Mecanica)
admin.site.register(Usuario)
admin.site.register(Prestamo)

class CustomUserAdmin(UserAdmin):
    model = Usuario
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('foto_perfil', 'fecha_nacimiento', 'mis_juegos')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('foto_perfil', 'fecha_nacimiento', 'mis_juegos')}),
    )
