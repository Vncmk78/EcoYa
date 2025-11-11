#from django.contrib import admin
from django.urls import path, include
from Producto import views

urlpatterns=[
    path('', views.Producto, name='producto'),
    path('create/', views.Create_producto, name='create_producto'),
    path('get/<int:id>', views.Get_producto, name='get_producto'),
    path('getall/', views.GetAll_producto, name='getall_producto'),
    path('update/<int:id>', views.Update_producto, name='update_producto'),
    path('delete/<int_id>', views.Delete_producto, name='delete_producto'),
    ]
