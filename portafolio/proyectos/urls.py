from django.urls import path
from proyectos import views

urlpatterns = [
    path('proyecto/crear/', views.crear, name='crear_projecto'),
]