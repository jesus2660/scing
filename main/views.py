#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from main.models import Proyecto
from main.file_parser import handle_file_import
from django.http.response import HttpResponseRedirect
from main.forms import UploadFileForm


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

def stats_yearly(request):
    """retira todos los proyectos activos (nuevos y renovados) durante el año
    seleccionado y genera las tablas y estadisticas del informe de gestion anual"""
    proyectos = Proyecto.objects.all().exclude(estatus="C")
    return render(request,'yearly.html',{"proyectos":proyectos})

def import_data(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            data = handle_file_import(request.FILES['file'])
            request.SESSION["data"]=data
            return HttpResponseRedirect('/importar/reporte/')
    else:
        form = UploadFileForm()
    return render(request, 'import.html', {"form":form})

def import_data_report(request):
    data = request.SESSION["data"]
    return render(request,'import_report.html',data)