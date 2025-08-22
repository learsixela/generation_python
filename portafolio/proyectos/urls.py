from django.urls import path
from proyectos import views

urlpatterns = [
    path('proyecto/listar/', views.listar_todos, name='listar_todos'),
    path('proyecto/crear/', views.crear, name='crear_projecto'),
    path('proyecto/<int:id>/editar/', views.editar, name='editar_projecto'),
    path('proyecto/<int:id>/eliminar/', views.eliminar, name='eliminar_projecto'),
]