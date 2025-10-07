from django.core.management.base import BaseCommand
from faker import Faker
from gestion_tareas.models import *

class Command(BaseCommand):
    help = "Generando datos usando Faker"
    
    def handle(self, *args, **kwargs):
        fake = Faker('es_ES')
        
        for _ in range(10):
            Usuario.objects.create(
                nombre = fake.name(),
                correo = fake.unique.email(),
                password  = fake.password(length=10)
            )
        
        self.stdout.write(self.style.SUCCESS('Datos generados correctamente'))