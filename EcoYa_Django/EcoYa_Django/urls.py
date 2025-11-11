"""
URL configuration for EcoYa_Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from Producto import views as producto_views
from . import views as proyecto_views
#from Producto import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('producto', views.inicio, name='inicio_producto'),
    path('producto/', include('Producto.urls')),
    path('', proyecto_views.index, name='index'),
    path('obtener/<int:id>', producto_views.Get_producto, name='obtener_producto'),
    path('actualizar/<int:id>', producto_views.Update_producto, name='actualizar_producto'),
    path('obtener_todos/', producto_views.GetAll_producto, name='obtener_todos'),
    path('crear/', producto_views.Create_producto, name='crear_producto'),
    path('eliminar/<int:id>', producto_views.Delete_producto, name='eliminar_producto'),
]
