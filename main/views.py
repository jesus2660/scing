#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
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

def stats_yearly(request):
    """retira todos los proyectos activos (nuevos y renovados) durante el año
    seleccionado y genera las tablas y estadisticas del informe de gestion anual"""
    proyectos = Proyecto.objects.all().exclude(estatus="C")
    return render(request,'yearly.html',{"proyectos":proyectos})