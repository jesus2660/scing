from django.contrib import admin
from main.models import *

class SemestreAdmin(admin.ModelAdmin):
    list_display = ("codido","fecha_inicio","fecha_final")

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos','ci','email_ula','email_alternativo','telefono','escuela')
    list_filter = ('escuela','proyecto','tutor')
    search_fields = ['nombres','apellidos','ci']
    
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos','ci','email_ula','telefono','numero_induccion')
    list_filter = ('escuela','estatus','facultad','unidad_academica')
    search_fields = ['nombres','apellidos','ci','numero_induccion']

class ComunidadAdmin(admin.ModelAdmin):
    list_display = ('nombre','rif','sector','parroquia','municipio','estado')
    search_fields = ['nombre']
    
class AsesorAdmin(admin.ModelAdmin):
    list_display = ('nombres','apellidos','ci','cargo','email','telefono','telefono_celular')
    search_fields = ['nombres','apellidos','ci']

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("__str__","estatus","responsable")
    list_filter = ("escuela","estatus")
    search_fields = ['codigo','titulo']
    
admin.site.register(Semestre,SemestreAdmin)
admin.site.register(Escuela)
admin.site.register(UnidadAcademica)
admin.site.register(Facultad)
admin.site.register(Comunidad,ComunidadAdmin)
admin.site.register(Asesor,AsesorAdmin)
admin.site.register(Profesor,ProfesorAdmin)
admin.site.register(Estudiante,EstudianteAdmin)
admin.site.register(Proyecto,ProyectoAdmin)
admin.site.register(Culminacion)
admin.site.register(Inscripcion)
admin.site.register(Exoneracion)
admin.site.register(Aprobacion)
admin.site.register(Reestructuracion)
admin.site.register(Renovacion)
admin.site.register(Cierre)
