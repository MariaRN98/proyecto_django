from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
from django.urls import reverse_lazy
from .forms import UsuarioCreationForm

# juegos
class ListadoJuegos(ListView):
    model = Juego
    template_name = 'aplicacion/juegos_listado.html'
    context_object_name = 'listado_juegos'

class DetalleJuego(DetailView):
    model = Juego
    template_name = 'aplicacion/juegos_detalle.html'
    context_object_name = 'detalle_juego'

class EditarJuego(UpdateView):
    model = Juego
    template_name = 'aplicacion/juegos_editar.html'
    context_object_name = 'editar_juego'
    fields = '__all__'
    success_url = reverse_lazy('listado_juegos')

# usuarios

class RegistroView(CreateView):
    form_class = UsuarioCreationForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')  # Redirige al login después del registro

class Detalleusuario(DetailView):
    model = Usuario
    template_name = 'aplicacion/usuario_detalle.html'
    context_object_name = 'detalle_usuario'