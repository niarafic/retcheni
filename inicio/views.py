from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from inicio.models import Staff

# Create your views here.
def inicio(request):
    return render(request, 'inicio/inicio.html')
def staff(request):
    staff=Staff(nombre='Rober', apellido='Etcheni', mail='retcheni@gmail.com')
    staff.save()
    return render(request, 'inicio/staff.html', {'miembro':staff})
    