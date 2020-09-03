from  django.http import HttpResponse
from django.template import Template
from django.shortcuts import render

def inicio (request):
    return render (request, 'inicio.htm')


def saludo (request):
    return HttpResponse('Bienvenidos a belleza y salud')

    def mensaje (request):
     return HttpResponse('Bienvenidos a belleza y salud')

    def inicio (request):
     return HttpResponse('Bienvenidos a belleza y salud')