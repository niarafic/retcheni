from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from inicio.models import Usuario

# Create your views here.
def inicio(request):
    return render(request, 'inicio/inicio.html')
def usuario(request):
    usuario=Usuario(nombre_usuario='Rober')
    
    return render(request, 'inicio/usuario.html', {'usuario':usuario})
    