from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('libros', views.libros, name='libros'),
    path('contacto', views.contacto, name='contacto')
]