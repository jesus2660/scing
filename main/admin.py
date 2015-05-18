from django.contrib import admin
from django.contrib.admin.models import LogEntry, DELETION
from django.core.urlresolvers import reverse
from django.utils.html import escape

from main.models import Semestre, Escuela, UnidadAcademica, Facultad, Comunidad, \
    Asesor, Profesor, Estudiante, Proyecto, Culminacion, Inscripcion, \
    Exoneracion, Aprobacion, Reestructuracion, Renovacion, Cierre


class SemestreAdmin(admin.ModelAdmin):
    list_display = ("codigo","fecha_inicio","fecha_final")

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos','ci','email_ula','email_alternativo','telefono_celular','escuela')
    list_filter = ('escuela','proyecto','tutor')
    search_fields = ['nombres','apellidos','ci']
    
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos','ci','email_ula','telefono_celular','numero_induccion')
    list_filter = ('escuela','estatus','facultad','unidad_academica')
    search_fields = ['nombres','apellidos','ci','numero_induccion']

class ComunidadAdmin(admin.ModelAdmin):
    list_display = ('nombre','rif','sector','parroquia','municipio','estado')
    search_fields = ['nombre']
    
class AsesorAdmin(admin.ModelAdmin):
    list_display = ('nombres','ci','cargo','email','telefono_institucional','telefono_celular')
    search_fields = ['nombres','apellidos','ci']

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("__str__","estatus","responsable")
    list_filter = ("facultad_adscripcion","estatus","numero_acta_aprobacion","fecha_aprobacion")
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



#LOGGING

class LogEntryAdmin(admin.ModelAdmin):

    date_hierarchy = 'action_time'

    readonly_fields = LogEntry._meta.get_all_field_names()  # @UndefinedVariable

    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    search_fields = [
        'object_repr',
        'change_message'
    ]


    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_link',
        'action_flag',
        'change_message',
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser and request.method != 'POST'

    def has_delete_permission(self, request, obj=None):
        return False

    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = u'<a href="%s">%s</a>' % (
                reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id]),
                escape(obj.object_repr),
            )
        return link
    object_link.allow_tags = True
    object_link.admin_order_field = 'object_repr'
    object_link.short_description = u'object'
    
    def queryset(self, request):
        return super(LogEntryAdmin, self).queryset(request) \
            .prefetch_related('content_type')


admin.site.register(LogEntry, LogEntryAdmin)