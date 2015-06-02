def unir_comunidades(modeladmin, request, queryset):
    if len(queryset)<2:
        return
    comunidad_elegida = queryset[0]
    for comunidad in queryset:
        for estudiante in comunidad.estudiante_set.all():
            estudiante.comunidad = comunidad_elegida
            estudiante.save()
        for asesor in comunidad.asesor_set.all():
            asesor.comunidad = comunidad_elegida
            asesor.save()
    for comunidad in queryset[1:len(queryset)]:
        comunidad.delete()
unir_comunidades.short_description = "Unir Comunidades repetidas selecionadas"


def unir_asesores(modeladmin, request, queryset):
    if len(queryset)<2:
        return
    asesor_elegido = queryset[0]
    for asesor in queryset:
        for estudiante in asesor.estudiante_set.all():
            estudiante.asesor = asesor_elegido
            estudiante.save()
    for asesor in queryset[1:len(queryset)]:
        asesor.delete()
unir_asesores.short_description = "Unir Asesores repetidos selecionadas"