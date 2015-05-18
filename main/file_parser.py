#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import codecs

from SCIng.settings import MEDIA_ROOT
from main.models import Estudiante, Escuela, Semestre, Profesor, Proyecto, \
    Facultad, Comunidad, Asesor


def clean_phone(token):
    token.replace(" ","")
    token.replace("-","")
    token.replace(",","")
    token.replace(";","")
    
    return token

def handle_file_import(f):
    """importa el archivo suministrado a la base de datos"""
    path = os.path.join(MEDIA_ROOT, 'csv')
    if not os.path.exists(path):
        os.mkdir(path)
        
    report_data = {"log":[], "filename":f.name}
    filename = os.path.join(MEDIA_ROOT, 'csv', f.name)
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        destination.close()
        
    
    with codecs.open(filename, "r","utf-8") as data:
        lines = data.readlines()
        i = 0
        for line in lines[1:len(lines)]:
            print i
            tokens = line.split(';')
            for token in tokens: token = token.encode("utf-8")
            
            # CREAR ESTUDIANTES
            
            estudiante = Estudiante(nombres=tokens[1],
                                    apellidos=tokens[2],
                                    ci=tokens[3],
                                    telefono_habitacion=clean_phone(tokens[4]),
                                    telefono_celular=clean_phone(tokens[5]),
                                    email_ula=tokens[6],
                                    email_alternativo=tokens[7],
                                    )
            
            # ESCUELA
            
            if not Escuela.objects.filter(nombre=tokens[8]):
                escuela = Escuela(nombre=tokens[8])
                escuela.save()
                report_data["log"].append(u"Agregada escuela \"%s\" (recuerde agregar codigo de esta escuela en la interfaz de administracion)" % escuela.nombre)
                estudiante.escuela = escuela
            else:
                estudiante.escuela = Escuela.objects.get(nombre=tokens[8])
            
            # SEMESTRE INDUCCION
            if not Semestre.objects.filter(codigo=tokens[9]):
                semestre = Semestre(codigo=tokens[9][0:6])
                report_data["log"].append(u"Agregado semestre \"%s\" (recuerde agregar fecha inicial y final de este semestre en la interfaz de administracion)" % semestre.codigo)
                semestre.save()
                estudiante.semestre_induccion = semestre
            else:
                estudiante.semestre_induccion = Semestre.objects.get(codigo=tokens[9])
                
            # TUTOR
            profesor = None
            if not Profesor.objects.filter(ci=tokens[11]):
                words = tokens[10].split()
                if len(words) > 2:
                    nombre = words[0]
                    apellido = words[1]
                else:
                    nombre = tokens[10]
                    apellido = u""
                profesor = Profesor(nombres=nombre,
                                    apellidos=apellido,
                                    ci=tokens[11],
                                    numero_induccion=tokens[17],
                                    estatus=u"A",
                                    email_ula=tokens[14],
                                    email_alternativo=tokens[15],
                                    telefono_oficina=clean_phone(tokens[12]),
                                    telefono_celular=clean_phone(tokens[13]),
                                    )
                if not Escuela.objects.filter(nombre=tokens[16]):
                    escuela = Escuela(nombre=tokens[16])
                    escuela.save()
                    report_data["log"].append(u"Agregada escuela \"%s\" (recuerde agregar código de esta escuela en la interfaz de administracion)" % escuela.nombre)
                    profesor.escuela = escuela
                else:
                    profesor.escuela = Escuela.objects.get(nombre=tokens[16])
                # report_data["log"].append(u"Agregado profesor \"%s %s\" (recuerde verificar si los datos son correctos y agregar los campos faltantes en la interfaz de administracion" % profesor)
                profesor.save()
                estudiante.tutor = profesor
            else:
                profesor = Profesor.objects.get(ci=tokens[11])
                estudiante.tutor = profesor
                
            # PROYECTO
            # TODO: manejar excepcion si len(tokens[18])<6
            codigo = tokens[18][0:4]
            titulo = tokens[18][6:len(tokens[18])]
            
            if not Proyecto.objects.filter(titulo=titulo):
                fecha = datetime.datetime.strptime(tokens[20], "%d-%m-%Y").date()
                facultad, created = Facultad.objects.get_or_create(nombre=tokens[19])
                if created:
                    report_data["log"].append(u"Agregada facultad \"%s\"" % tokens[19])
                proyecto = Proyecto(codigo=codigo,
                                    titulo=titulo,
                                    responsable=profesor,
                                    fecha_aprobacion=fecha,
                                    numero_acta_aprobacion=tokens[21],
                                    facultad_adscripcion=facultad,
                                    estatus=u"A",)
                proyecto.save()
                proyecto.tutores.add(profesor)
                report_data["log"].append("Agregado proyecto \"%s\" (recuerde verificar si los datos de este proyecto son correctos en la interfaz de administracion, se ha asumido a %s como responsable del proyecto" % (proyecto.titulo, proyecto.responsable))
                profesor.save()
                estudiante.proyecto = proyecto
            else:
                proyecto = Proyecto.objects.get(titulo=titulo)
                estudiante.proyecto = proyecto
                
            # COMUNIDAD Y ASESOR COMUNITARIO
            comunidad = None
            if not Comunidad.objects.filter(rif=tokens[23]):
                comunidad = Comunidad(nombre=tokens[22],
                                      rif=tokens[23],
                                      sector=tokens[24],
                                      parroquia=tokens[25],
                                      municipio=tokens[26],
                                      estado=tokens[27],
                )
                comunidad.save()
                report_data["log"].append("Agregada comunidad \"%s\"" % comunidad.nombre)
                estudiante.comunidad = comunidad
            else:
                comunidad = Comunidad.objects.get(rif=tokens[23])
                estudiante.comunidad = comunidad 
                
            asesor, created = Asesor.objects.get_or_create(nombres=tokens[28],
                                                           email=tokens[31],
                                                           telefono_institucional=clean_phone(tokens[29]),
                                                           telefono_celular=clean_phone(tokens[30]),
                                                           cargo=tokens[32],
                                                           comunidad=comunidad)
            estudiante.asesor = asesor
            estudiante.save()
            if created:
                report_data["log"].append("Agregado asesor comunitario \"%s\" (recuerde verificar si los datos son correctos)" % asesor.nombres)

            i += 1
        report_data["students"] = i      
    return report_data