#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.aggregates import Max


class TruncatingCharField(models.CharField):
    def get_prep_value(self, value):
        value = super(TruncatingCharField,self).get_prep_value(value)
        if value:
            return value[:self.max_length]
        return value

class Escuela(models.Model):
    nombre = TruncatingCharField(max_length=64);
    codigo = TruncatingCharField(max_length=16);
    
    def __unicode__(self):
        return "%s [%s]" % (self.nombre,self.codigo)
    

class Semestre(models.Model):
    codigo = TruncatingCharField(max_length=16)
    fecha_inicio = models.DateField(blank=True,null=True)
    fecha_final = models.DateField(blank=True,null=True)
    
    def __unicode__(self):
        return self.codigo


class UnidadAcademica(models.Model):
    nombre = TruncatingCharField(max_length=64);
    codigo = TruncatingCharField(max_length=16);
    
    class Meta:
        verbose_name_plural = "Unidades Academicas"
        
    def __unicode__(self):
        return "%s [%s]" % (self.nombre,self.codigo)

class Facultad(models.Model):
    nombre = TruncatingCharField(max_length=64);

    class Meta:
        verbose_name_plural = "Facultades"
        
    def __unicode__(self):
        return self.nombre
    
    
class Comunidad(models.Model):
    nombre = TruncatingCharField(max_length=128)
    rif = TruncatingCharField(max_length=16)
    sector = TruncatingCharField(max_length=64)
    parroquia = TruncatingCharField(max_length=64)
    municipio = TruncatingCharField(max_length=64)
    estado = TruncatingCharField(max_length=64)
    
    class Meta:
        verbose_name_plural = "Comunidades"
        
    def __unicode__(self):
        return self.nombre
    

ESTATUS_ESTUDIANTE = (
    ("I", 'Inscrito'),
    ("C", 'Culminado'),
) 

class Estudiante(models.Model):
    nombres = TruncatingCharField(max_length=32)
    apellidos = TruncatingCharField(max_length=32)
    ci = TruncatingCharField(max_length=10,verbose_name="CI");
    email_ula = models.EmailField(blank=True)
    email_alternativo = models.EmailField()
    telefono_habitacion = TruncatingCharField(max_length=12)
    telefono_celular = TruncatingCharField(max_length=12)
    escuela = models.ForeignKey(Escuela)
    semestre_induccion = models.ForeignKey(Semestre,related_name="induccion_est_set",blank=True,null=True)
    semestre_inscripcion = models.ForeignKey(Semestre,related_name="inscripccion_est_set",blank=True,null=True)
    semestre_culminacion = models.ForeignKey(Semestre,related_name="culminacion_est_set",blank=True,null=True)
    proyecto = models.ForeignKey("Proyecto",blank=True,null=True)
    tutor = models.ForeignKey("Profesor",blank=True,null=True)
    comunidad  = models.ForeignKey("Comunidad",blank=True,null=True)
    asesor = models.ForeignKey("Asesor",blank=True,null=True)
    estatus = models.CharField(max_length=1, choices=ESTATUS_ESTUDIANTE,default="I")
    
    def __unicode__(self):
        return "%s %s" % (self.nombres, self.apellidos)


ESTATUS_PROFESOR = (
    ("I", 'Inactivo'),
    ("A", 'Activo'),
) 

class Profesor(models.Model):
    nombres = TruncatingCharField(max_length=32)
    apellidos = TruncatingCharField(max_length=32)
    ci = TruncatingCharField(max_length=10,verbose_name="CI")
    escuela = models.ForeignKey(Escuela,blank=True,null=True)
    unidad_academica = models.ForeignKey(UnidadAcademica,blank=True,null=True)
    facultad = models.ForeignKey(Facultad,blank=True,null=True)
    numero_induccion = TruncatingCharField(max_length=10,verbose_name="número de inducción")
    estatus = TruncatingCharField(max_length=1, choices=ESTATUS_PROFESOR)
    email_ula = models.EmailField()
    email_alternativo = models.EmailField()
    telefono_oficina = TruncatingCharField(max_length=12)
    telefono_celular = TruncatingCharField(max_length=12,blank=True)
    
    class Meta:
        verbose_name_plural = "Profesores"
        
    def __unicode__(self):
        return "%s %s" % (self.nombres,self.apellidos)

class Asesor(models.Model):
    nombres = TruncatingCharField(max_length=64)
    ci = TruncatingCharField(max_length=10,verbose_name="CI",blank=True);
    email = models.EmailField()
    telefono_institucional = TruncatingCharField(max_length=12)
    telefono_celular = TruncatingCharField(max_length=12)
    cargo = TruncatingCharField(max_length=256)
    comunidad = models.ForeignKey(Comunidad)
    
    class Meta:
        verbose_name_plural = "Asesores"
        
    def __unicode__(self):
        return "%s (%s)" % (self.nombres,self.cargo)
    
    
    
ESTATUS_PROYECTO = (
    ("A", 'Aprobado'),
    ("R", 'Renovado'),
    ("C", 'Cerrado'),
)     

class Proyecto(models.Model):
    codigo = TruncatingCharField(max_length=4)
    titulo = TruncatingCharField(max_length=256)
    responsable = models.ForeignKey(Profesor,related_name="responsable_set")
    tutores = models.ManyToManyField(Profesor,related_name="tutor_set")
    fecha_aprobacion = models.DateField(verbose_name="fecha de aprobación")
    numero_acta_aprobacion = TruncatingCharField(max_length=16)
    facultad_adscripcion = models.ForeignKey(Facultad)
    archivo = models.FileField(upload_to="proyectos",blank=True,null=True)
    estatus = TruncatingCharField(max_length=1, choices=ESTATUS_PROYECTO)

    def __unicode__(self):
        return "[%s] %s" % (self.codigo,self.titulo)

ESTATUS_CULMINACION  = (
    ("P", 'Pendiente'),
    ("C", 'Culminado'),
    ("P", 'En proceso'),
) 

class Culminacion(models.Model):
    estudiante = models.ForeignKey(Estudiante)
    semestre = models.ForeignKey(Semestre,related_name="culminacion_set")
    oficio = models.FileField(upload_to="culminaciones")
    fecha_cesc_csscfi = models.DateField(verbose_name="Fecha de trámite CESC ante CSSCFI")
    fecha_csscfi_ccscula = models.DateField(verbose_name="Fecha de trámite CSSCFI ante CCSCULA")
    numero_oficio = TruncatingCharField(max_length=16,verbose_name="número de oficio")
    estatus = TruncatingCharField(max_length=1, choices=ESTATUS_CULMINACION)
    
    class Meta:
        verbose_name_plural = "Culminaciones"
    
    
class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante)
    semestre = models.ForeignKey(Semestre)
    fecha_cesc_csscfi = models.DateField(verbose_name="Fecha de trámite CESC ante la CSSCFI")
    fecha_csscfi_orefi = models.DateField(verbose_name="Fecha de trámite CSSCFI ante OREFI",blank=True)
    numero_oficio = TruncatingCharField(max_length=16,verbose_name="número de oficio")
    carta_aceptacion_tutor = models.FileField(upload_to = "inscripciones",verbose_name="carta de aceptacion del tutor")
    carta_aceptacion_comunidad = models.FileField(upload_to = "inscripciones",verbose_name="carta de aceptacion de la comunidad")
    programa_actividades = models.FileField(upload_to = "inscripciones",verbose_name="programa de actividades del estudiante")
    aval_ce_induccion = models.FileField(upload_to = "inscripciones",verbose_name="Aval del CE para cursar Induccion y SC",blank=True,null=True)
    aval_ce_proyecto = models.FileField(upload_to = "inscripciones",verbose_name="Aval del CE para realizar proyecto externo",blank=True,null=True)
    
    class Meta:
        verbose_name_plural = "Inscripciones"
        
class Exoneracion(models.Model):
    estudiante = models.ForeignKey(Estudiante)
    fecha = models.DateField()
    estudiante = models.ForeignKey(Estudiante)
    
    
class Aprobacion(models.Model):
    fecha = models.DateField()
    formato_proyecto = models.FileField(upload_to="proyectos/aprobaciones",blank=True)
    proyecto = models.ForeignKey(Proyecto)
    
    class Meta:
        verbose_name_plural = "Aprobaciones"
    

class Renovacion(models.Model):
    fecha = models.DateField()
    formato_proyecto = models.FileField(upload_to="proyectos/renovaciones/",blank=True)
    informe_tutor = models.FileField(upload_to="proyectos/renovaciones/",blank=True)
    proyecto = models.ForeignKey(Proyecto)
    
    class Meta:
        verbose_name_plural = "Renovaciones"
    
    
class Reestructuracion(models.Model):
    fecha = models.DateField()
    formato_proyecto = models.FileField(upload_to="proyectos/reestructuraciones/",blank=True)
    informe_tutor = models.FileField(upload_to="proyectos/reestructuraciones/",blank=True)
    proyecto = models.ForeignKey(Proyecto)
    
    class Meta:
        verbose_name_plural = "Reestructuraciones"

class Cierre(models.Model):
    fecha = models.DateField()
    formato_proyecto = models.FileField(upload_to="proyectos/cierres/",blank=True)
    informe_cierre = models.FileField(upload_to="proyectos/cierres/",blank=True)
    proyecto = models.ForeignKey(Proyecto)