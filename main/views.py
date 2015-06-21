#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from main.file_parser import handle_file_import_total,\
    handle_file_import_partial
from main.forms import UploadFileForm
from main.models import Proyecto


def index(request):
    """muestra la pagina principal"""
    return render(request,'index.html',{})

def manual(request):
    """muestra el manual de uso"""
    return render(request,'manual.html',{})

def docs(request):
    """muestra la documentacion"""
    return render(request,'docs.html',{})

def stats(request):
    """muestra el formulario para desplegar los distintos informes y 
    estadisticas disponibles a partir de la informacion de la base de datos"""
    return render(request,'stats.html',{})

def report(request):
    """retira todos los proyectos activos (nuevos y renovados) durante el año
    seleccionado y genera las tablas y estadisticas del informe de gestion anual"""
    proyectos = Proyecto.objects.all().exclude(estatus="C")
    return render(request,'report.html',{"proyectos":proyectos})

def memory(request):
    pass

def import_data(request):
    return render(request, 'import.html',{})

def import_total(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            data = handle_file_import_total(request.FILES['file'])
            request.session["data"]=data
            return HttpResponseRedirect('/importar/reporte/')
    else:
        form = UploadFileForm()
    return render(request, 'import_total.html', {"form":form})

def import_partial(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            data = handle_file_import_partial(request.FILES['file'])
            request.session["data"]=data
            return HttpResponseRedirect('/importar/reporte/')
    else:
        form = UploadFileForm()
    return render(request, 'import_partial.html', {"form":form})

def import_data_report(request):
    data = request.session["data"]
    return render(request,'import_report.html',data)