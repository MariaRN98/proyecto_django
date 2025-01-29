from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('juegos/', ListadoJuegos.as_view(), name='listado_juegos'),
    path('juegos/<int:pk>', DetalleJuego.as_view(), name='detalle_juego'),
    path('juegos/<int:pk>/edit', DetalleJuego.as_view(), name='editar_juego'),
]