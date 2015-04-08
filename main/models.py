#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class Escuela(models.Model):
    nombre = models.CharField(max_length=64);
    codigo = models.CharField(max_length=16);
    
    def __unicode__(self):
        return "%s [%s]" % (self.nombre,self.codigo)
    

class Semestre(models.Model):
    codido = models.CharField(max_length=6)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    
    def __unicode__(self):
        return self.codido
    

class UnidadAcademica(models.Model):
    nombre = models.CharField(max_length=64);
    codigo = models.CharField(max_length=16);
    
    class Meta:
        verbose_name_plural = "Unidades Academicas"
        
    def __unicode__(self):
        return "%s [%s]" % (self.nombre,self.codigo)

class Facultad(models.Model):
    nombre = models.CharField(max_length=64);

    class Meta:
        verbose_name_plural = "Facultades"
        
    def __unicode__(self):
        return self.nombre
    
    
class Comunidad(models.Model):
    nombre = models.CharField(max_length=64)
    rif = models.CharField(max_length=16)
    sector = models.CharField(max_length=64)
    parroquia = models.CharField(max_length=64)
    municipio = models.CharField(max_length=64)
    estado = models.CharField(max_length=64)
    asesor = models.ForeignKey("Asesor",blank=True,null=True)
    
    class Meta:
        verbose_name_plural = "Comunidades"
        
    def __unicode__(self):
        return self.nombre
    

class Estudiante(models.Model):
    nombres = models.CharField(max_length=32)
    apellidos = models.CharField(max_length=32)
    ci = models.CharField(max_length=10,verbose_name="CI");
    email_ula = models.EmailField(blank=True)
    email_alternativo = models.EmailField()
    telefono = models.CharField(max_length=11)
    escuela = models.ForeignKey(Escuela)
    semestre_induccion = models.ForeignKey(Semestre,related_name="induccion_est_set",blank=True,null=True)
    semestre_inscripcion = models.ForeignKey(Semestre,related_name="inscripccion_est_set",blank=True,null=True)
    semestre_culminacion = models.ForeignKey(Semestre,related_name="culminacion_est_set",blank=True,null=True)
    proyecto = models.ForeignKey("Proyecto",blank=True,null=True)
    tutor = models.ForeignKey("Profesor",blank=True,null=True)
    comunidad  = models.ForeignKey("Comunidad",blank=True,null=True)
    
    def __unicode__(self):
        return "%s %s" % self.nombres + self.apellidos


ESTATUS_PROFESOR = (
    ("I", 'Inactivo'),
    ("A", 'Activo'),
) 

class Profesor(models.Model):
    nombres = models.CharField(max_length=32)
    apellidos = models.CharField(max_length=32)
    ci = models.CharField(max_length=10,verbose_name="CI")
    escuela = models.ForeignKey(Escuela)
    unidad_academica = models.ForeignKey(UnidadAcademica)
    facultad = models.ForeignKey(Facultad)
    numero_induccion = models.CharField(max_length=10,verbose_name="número de inducción")
    estatus = models.CharField(max_length=1, choices=ESTATUS_PROFESOR)
    email_ula = models.EmailField()
    email_alternativo = models.EmailField()
    telefono = models.CharField(max_length=11)
    
    class Meta:
        verbose_name_plural = "Profesores"
        
    def __unicode__(self):
        return "%s %s" % self.nombres + self.apellidos

class Asesor(models.Model):
    nombres = models.CharField(max_length=32)
    apellidos = models.CharField(max_length=32)
    ci = models.CharField(max_length=10,verbose_name="CI");
    email = models.EmailField()
    telefono = models.CharField(max_length=11)
    telefono_celular = models.CharField(max_length=11)
    cargo = models.CharField(max_length=64)
    
    class Meta:
        verbose_name_plural = "Asesores"
        
    def __unicode__(self):
        return "%s (%s)" % (self.nombre,self.cargo)
    
    
    
ESTATUS_PROYECTO = (
    ("A", 'ARPOBADO'),
    ("R", 'RENOVADO'),
    ("C", 'CERRADO'),
)     

class Proyecto(models.Model):
    codigo = models.CharField(max_length=4)
    titulo = models.CharField(max_length=64)
    responsable = models.ForeignKey(Profesor,related_name="responsable_set")
    tutores = models.ManyToManyField(Profesor,related_name="tutor_set")
    fecha_aprobacion = models.DateField(verbose_name="fecha de aprobación")
    numero_acta_aprobacion = models.CharField(max_length=16)
    escuela = models.ForeignKey(Escuela)
    unidad_academica = models.ForeignKey(UnidadAcademica)
    archivo = models.FileField(upload_to="proyectos")
    asesor = models.ForeignKey(Asesor)
    estatus = models.CharField(max_length=1, choices=ESTATUS_PROYECTO)

    def __unicode__(self):
        return "[%s] %s" % (self.codigo,self.titulo)

ESTATUS_CULMINACION  = (
    ("P", 'PENDIENTE'),
    ("C", 'CULMINADO'),
    ("P", 'EN PROCESO'),
) 

class Culminacion(models.Model):
    semestre = models.ForeignKey(Semestre,related_name="culminacion_set")
    oficio = models.FileField(upload_to="culminaciones")
    fecha_cesc_csscfi = models.DateField(verbose_name="Fecha de trámite CESC ante CSSCFI")
    fecha_csscfi_ccscula = models.DateField(verbose_name="Fecha de trámite CSSCFI ante OREFI")
    numero_oficio = models.CharField(max_length=16,verbose_name="número de oficio")
    estatus = models.CharField(max_length=1, choices=ESTATUS_CULMINACION)
    
    class Meta:
        verbose_name_plural = "Culminaciones"
    
    
class Inscripcion(models.Model):
    semestre = models.ForeignKey(Semestre)
    fecha_cesc_csscfi = models.DateField(verbose_name="Fecha de trámite CESC ante la CSSCFI")
    fecha_csscfi_orefi = models.DateField(verbose_name="Fecha de trámite CSSCFI ante la CCSCULA")
    numero_oficio = models.CharField(max_length=16,verbose_name="número de oficio")
    carta_aceptacion_tutor = models.FileField(upload_to = "inscripciones",verbose_name="carta de aceptacion del tutor")
    carta_aceptacion_comunidad = models.FileField(upload_to = "inscripciones",verbose_name="carta de aceptacion de la comunidad")
    programa_actividades = models.FileField(upload_to = "inscripciones",verbose_name="programa de actividades del estudiante")
    aval_ce_induccion = models.FileField(upload_to = "inscripciones",verbose_name="Aval del CE para cursar Induccion y SC")
    aval_ce_proyecto = models.FileField(upload_to = "inscripciones",verbose_name="Aval del CE para realizar proyecto externo")
    
    class Meta:
        verbose_name_plural = "Inscripciones"
        
class Exoneracion(models.Model):
    fecha = models.DateField()
    estudiante = models.ForeignKey(Estudiante)
    
    
class Aprobacion(models.Model):
    fecha = models.DateField()
    formato_proyecto = models.FileField(upload_to="proyectos")
    proyecto = models.ForeignKey(Proyecto)
    
    class Meta:
        verbose_name_plural = "Aprobaciones"
    

class Renovacion(models.Model):
    fecha = models.DateField()
    formato_proyecto = models.FileField(upload_to="proyectos")
    informe_tutor = models.FileField(upload_to="proyectos")
    proyecto = models.ForeignKey(Proyecto)
    
    class Meta:
        verbose_name_plural = "Renovaciones"
    
    
class Reestructuracion(models.Model):
    fecha = models.DateField()
    formato_proyecto = models.FileField(upload_to="proyectos")
    informe_tutor = models.FileField(upload_to="proyectos")
    proyecto = models.ForeignKey(Proyecto)
    
    class Meta:
        verbose_name_plural = "Reestructuraciones"

class Cierre(models.Model):
    fecha = models.DateField()
    formato_proyecto = models.FileField(upload_to="proyectos")
    informe_cierre = models.FileField(upload_to="proyectos")
    proyecto = models.ForeignKey(Proyecto)