from django.contrib import admin
from .models import Usuario,Asignacion_Tarea,Comentario,Etiqueta,Proyecto,Tarea

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Tarea)
admin.site.register(Proyecto)
admin.site.register(Etiqueta)
admin.site.register(Comentario)
admin.site.register(Asignacion_Tarea)