from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(default=timezone.now)

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    
    usuarios_asignados = models.ManyToManyField(Usuario,related_name="proyectos_usuarios")
    creador = models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Tarea(models.Model):
    ESTADOS = [
        ("PEN","Pendiente"),
        ("PRO","Progreso"),
        ("COM","Completada"),
    ]
    
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    estado = models.CharField(
        max_length=3,
        choices=ESTADOS,
        default="PEN",
    )
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateField()
    hora_vencimiento = models.TimeField()
    
    usuarios_asignados = models.ManyToManyField(Usuario,through='Asignacion_Tarea', related_name="tareas_usuarios")
    creador = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100,unique=True)
    
    tareas_asignadas = models.ManyToManyField(Tarea, related_name="etiquetas_tareas")

class Asignacion_Tarea(models.Model):
    obsevaciones = models.TextField()
    fecha_asignacion = models.DateTimeField(default=timezone.now)
    
    tarea = models.ForeignKey(Tarea,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Comentario(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(default=timezone.now)
    
    autor = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea,on_delete=models.CASCADE)
