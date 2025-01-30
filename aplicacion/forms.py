from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()  # Esto asegura que use tu modelo personalizado
        fields = ('username', 'email', 'first_name', 'last_name', 'foto_perfil', 'fecha_nacimiento', 'mis_juegos')  # Ajusta los campos según tu modelo