from django.contrib import admin
from django.urls import path, include
from app_cosillas import views

urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),   # la página principal
    path('producto/', views.app_cosillas, name='producto'),
    path('base/', views.base, name='base'),
    path("mapa/", views.mapa, name="mapa"),
    path("puntos/", views.puntos, name="puntos"),
    path("contacto/", views.contacto, name="contacto"),
]
