from django.urls import path
from proyectos import views
from .views_api import proyectos_collection, proyecto_item

urlpatterns = [
    path('', views.listar_todos, name='listar_todos'),
    path('proyecto/crear/', views.crear, name='crear_projecto'),
    path('proyecto/<int:id>/editar/', views.editar, name='editar_projecto'),
    path('proyecto/<int:id>/eliminar/', views.eliminar, name='eliminar_projecto'),
    
    #urls api RestFull
    #GET    /api/proyectos/ -> detalle todos
    #POST   /api/proyectos/ -> crear
    path("api/proyectos/",proyectos_collection, name="proyectos_collection"),
    
    #GET    /api/proyectos/{id} -> detalle individual
    #PUT    /api/proyectos/{id} -> actualizar todos
    #PATCH  /api/proyectos/{id} -> actualizar parcial
    #DELETE /api/proyectos/{id} -> eliminar
    
    path("api/proyectos/<int:pk>",proyecto_item, name="proyecto_item"),
]