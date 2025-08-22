from django.urls import path
from proyectos import views

urlpatterns = [
    path('proyecto/listar/', views.listar_todos, name='listar_todos'),
    path('proyecto/crear/', views.crear, name='crear_projecto'),
    
]