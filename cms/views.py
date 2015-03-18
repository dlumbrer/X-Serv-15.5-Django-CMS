from django.shortcuts import render
from models import Pages
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def mostrar(request, recurso):
    try:
        fila = Pages.objects.get(name=recurso)
        print fila.name
        return HttpResponse(request.method + " " + str(fila.id) + " " + fila.name + " " + fila.page)
    except Pages.DoesNotExist:
        return HttpResponseNotFound("Page not found: " + recurso)

#OJO, la base de datos solo tiene /pepe y /pepito
