from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyecto 

# Create your views here.
#seleccionar todos
def listar_todos(request):
    #obtener todos los proyectos
    proyectos = Proyecto.objects.all()
    context = {
        "proyectos": proyectos
    }
    return render(request, "listar_proyectos.html",context )
    
#crear
def crear(request):
    
    if request.method == "GET":
        #despliegue del formulario
        print(request.GET) 
        return render(request, "crear_proyecto.html" )

    if request.method == "POST":
        #capturar los parametros        
        #print(request.POST)
        #print(request.POST["nombre"])
        #print(request.POST["descripcion"])
        nombre = request.POST["nombre"]
        descripcion= request.POST["descripcion"]
        link = request.POST["link"]
        
        #variable que sera capturada/leida desde otro html 
        context = {
            "nombre" : nombre,
            "descripcion":descripcion,
            "link": link
        }
        
        #guardar informacion en base datos
        Proyecto.objects.create(nombre=nombre,descripcion=descripcion,link=link   )
        
        #return render(request, "mostrar_proyecto.html",context ) 
        return redirect("listar_todos")
    
#seleccionar 1
#actualizar
def editar(request,id):
    proyecto = get_object_or_404(Proyecto,pk = id)
    if request.method == "GET":
        #enviar al html el proyecto
        context = {
            "proyecto": proyecto
        }
        return render(request,"mostrar_proyecto.html",context)
    
    #mostrar formulario pre cargado
    
    #metodo post
    if request.method == "POST":
        #setear los nuevos datos a los atributos
        proyecto.nombre = request.POST["nombre"]
        proyecto.descripcion = request.POST["descripcion"]
        proyecto.link = request.POST["link"]
        proyecto.save()
        return redirect("listar_todos") 
    
#eliminar
def eliminar(request,id):
    proyecto = get_object_or_404(Proyecto,pk = id)
    proyecto.delete()
    return redirect("listar_todos")