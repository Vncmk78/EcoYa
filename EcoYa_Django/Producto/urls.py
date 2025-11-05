#from django.contrib import admin
from django.urls import path, include
from Producto import views

urlpatterns=[
    path('', views.Producto, name='producto'),
    path('Create/', views.Create_producto, name='create_producto'),
    path('Get/<id>', views.Get_producto, name='get_producto'),
    path('GetAll/', views.GetAll_producto, name='getall_producto'),
    path('Update/', views.Update_producto, name='update_producto'),
    path('Delete/', views.Delete_producto, name='delete_producto'),
    ]
