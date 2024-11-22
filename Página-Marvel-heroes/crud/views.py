from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import marvel

# Create your views here.


def menu(request):
    
    lista_marvel= marvel.objects.all()
    template = loader.get_template("menu.html")
    
    context = {"marvel":lista_marvel}
    return HttpResponse(template.render(context,request))


def index(request):
    
    lista_marvel= marvel.objects.all()
    template = loader.get_template("index.html")
    
    context = {"marvel":lista_marvel}
    return HttpResponse(template.render(context,request))

def vista_detalle(request,id_marvel):
    detalle_marvel=marvel.objects.get(id=id_marvel)
    
    template= loader.get_template("detail.html")
    
    context= {"marvel":detalle_marvel}
    return HttpResponse(template.render(context,request))

