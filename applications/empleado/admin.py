from django.contrib import admin
from .models import Empleado, Habilidades


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job', 'department', 'active',)
    search_fields = ('first_name', 'last_name')
    list_filter = ('job', 'department', 'active', 'habilidades',)


    #FILTRO QUE SOLO FUNCIONA CON RELACIONES MUCHOS A MUCHOS (SE VE AL AGREGAR O EDITAR DE EMPLEADO)
    filter_horizontal = ('habilidades',)


admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)
