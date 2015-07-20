#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from main.file_parser import handle_file_import_total, \
    handle_file_import_partial
from main.forms import UploadFileForm
from main.models import Proyecto, Facultad, Profesor, Escuela, Culminacion, \
    Semestre, Estudiante


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
    render_data = {}
    year = request.GET["year"]
    render_data["year"]=year
    
    #excluimos los proyectos cerrados estatus="C"
    proyectos = Proyecto.objects.all().exclude(estatus="C")
    render_data["proyectos"]=proyectos
    nuevos = Proyecto.objects.filter(estatus="A").count()
    renovados = Proyecto.objects.filter(estatus="R").count()
    porcentaje_nuevos = str(nuevos/float(len(proyectos))*100)
    porcentaje_renovados = str(renovados/float(len(proyectos))*100)
    
    render_data.update({"nuevos":nuevos,"renovados":renovados,"porcentaje_nuevos":porcentaje_nuevos,"porcentaje_renovados":porcentaje_renovados})
    
    facultades = Facultad.objects.all()
    resultados_facultad = []
    total_facultades = Facultad.objects.count()
    for facultad in facultades:
        count = facultad.proyecto_set.exclude(estatus="C").count()
        if count > 0:
            resultados_facultad.append((facultad.nombre,str(float(count)/total_facultades*100)))
    
    render_data["facultades"]=resultados_facultad
    
    oferta_por_carreras = {}
    for escuela in Escuela.objects.all():
        oferta_por_carreras[escuela.nombre]=0
    
    for proyecto in proyectos:
        oferta_por_carreras[proyecto.responsable.escuela.nombre]+=1/float(len(proyectos))*100

    render_data["oferta_por_carreras"] = oferta_por_carreras
    
    #esto hay que cambiarlo por unidad academica
    responsables_por_escuela = oferta_por_carreras
    for key in responsables_por_escuela.keys():
        responsables_por_escuela[key]=0
        
    for proyecto in proyectos:
        responsables_por_escuela[proyecto.responsable.escuela.nombre]+=1
    
    render_data["responsables_por_escuela"] = oferta_por_carreras
    
    profesores = []
    for profesor in Profesor.objects.filter(estatus="A"):
        count = profesor.responsable_set.count()
        if count > 0:
            profesores.append((profesor,count))
    
    render_data["profesores_responsables"]=profesores
    
    culminaciones = Culminacion.objects.filter(fecha__year=year)
    num_culminaciones = len(culminaciones)
    proyectos_ejecutados = []
    tutores_de_proyectos_ejecutados = []
    comunidades_atendidas = []
    
    #tomamos los semestres que se hayan cursado durante el año elegido
    semestres_cursados = Semestre.objects.filter(fecha_final__gt='%s-01-01'%year).exclude(fecha_inicio__gt='%s-12-31'%year).order_by("fecha_inicio")
    semestre_data = {}
    estudiantes_por_escuela = {}
    estudiantes_por_semestre_escuela = {}
    
    for semestre in semestres_cursados:
        estudiantes_por_semestre_escuela[semestre]={}
        semestre_data[semestre]=[0,0,0,0]
        for escuela in Escuela.objects.all():
            estudiantes_por_semestre_escuela[semestre][escuela]=0
        
    tutores_por_escuela = {}
    for escuela in Escuela.objects.all():
        estudiantes_por_escuela[escuela]= 0
        tutores_por_escuela[escuela]=0
        
        
    for culminacion in culminaciones:
        semestre_data[semestre][2]+=1
        proyecto = culminacion.estudiante.proyecto
        semestre = culminacion.semestre
        
        if not proyecto in proyectos_ejecutados:
            proyectos_ejecutados.append(proyecto)
            semestre_data[semestre][0]+=1
            
        profesor = culminacion.estudiante.tutor
        escuela = culminacion.estudiante.escuela
        estudiantes_por_escuela[escuela]+=1
        estudiantes_por_semestre_escuela[semestre][escuela]+=1
        if not profesor in tutores_de_proyectos_ejecutados:
            tutores_de_proyectos_ejecutados.append(profesor)
            tutores_por_escuela[profesor.escuela]+=1
            semestre_data[semestre][1]+=1
            
        comunidad = culminacion.estudiante.comunidad
        if not comunidad in comunidades_atendidas:
            comunidades_atendidas.append(comunidad)
            semestre_data[semestre][3]+=1
        
    
    render_data.update({"num_culminaciones":num_culminaciones,
                        "proyectos_ejecutados":proyectos_ejecutados,
                        "tutores_de_proyectos_ejecutados":tutores_de_proyectos_ejecutados,
                        "comunidades_atendidas":comunidades_atendidas,
                        "semestres_cursados":semestres_cursados,
                        "estudiantes_por_escuela":estudiantes_por_escuela,
                        "tutores_por_escuela": tutores_por_escuela,
                        "estudiantes_por_semestre_escuela":estudiantes_por_semestre_escuela,
                        "semestre_data":semestre_data})
    
    return render(request,'report.html',render_data)
    

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