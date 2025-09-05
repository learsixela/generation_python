import json
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Proyecto

@csrf_exempt
def proyectos_collection(request):
    #GET    /api/proyectos/ -> detalle todos
    if request.method == "GET":
        proyectos = Proyecto.objects.all()
        
        data = [] #arreglo vacio
        for proyecto in proyectos:
            #crear diccionario
            dicc = {
                "id":proyecto.id,
                "nombre":proyecto.nombre,
                "descripcion":proyecto.descripcion,
                "link":proyecto.link,
                #"imagen":proyecto.image,
            }
            data.append(dicc)#agrego el diccionario al arreglo
        return JsonResponse(data,safe=False,status=200)
    
    
    #POST   /api/proyectos/ -> crear
    if request.method == "POST":
        #recibir informacion
        data= json.loads(request.body or "{}")
        #pendiente las validaciones
        
        print(data)#recibo un diccionario
        
        name = data.get("nombre")
        if not name:
            return JsonResponse({"Info:Nombre es obligatorio"}, status=400)
        
        desc = data.get("descripcion")
        
        #guardar informacion en base datos
        proyecto= Proyecto.objects.create(nombre=name,
                                descripcion=desc,
                                link=data.get("link") )
        
        data = [] #arreglo vacio
       
        #crear diccionario
        dicc2 = {
                "id":proyecto.id,
                "nombre":proyecto.nombre,
                "descripcion":proyecto.descripcion,
                "link":proyecto.link,
                #"imagen":proyecto.image,
            }
        data.append(dicc2)
        
        return JsonResponse(data,safe=False,status=200)

@csrf_exempt
def proyecto_item(request,pk):
    #GET    /api/proyectos/{id} -> detalle individual
    proyecto = get_object_or_404(Proyecto,pk = pk)
    if request.method == "GET":
        data = [] #arreglo vacio
       
        #crear diccionario
        dicc2 = {
                "id":proyecto.id,
                "nombre":proyecto.nombre,
                "descripcion":proyecto.descripcion,
                "link":proyecto.link,
                #"imagen":proyecto.image,
            }
        data.append(dicc2)
        
        return JsonResponse(data,safe=False,status=200)
    
    #PUT    /api/proyectos/{id} -> actualizar todos
    
    #PATCH  /api/proyectos/{id} -> actualizar parcial
    
    #DELETE /api/proyectos/{id} -> eliminar
    if request.method == "DELETE":
        proyecto.delete()
   