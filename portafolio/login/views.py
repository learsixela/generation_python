from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("""
                        <h1> Hola, soy Mijail </h1>
                        """)
    
def contacto(request):
    return HttpResponse("""
                        <h1>  Contacto </h1>
                        <form action="/contacto" method="post">
                            Nombre: <input type="text" name="nombre"><br>
                            Mensaje: <textarea name="mensaje"></textarea>
                            <input type="submit" value="enviar">
                        </form>
                        
                        """)