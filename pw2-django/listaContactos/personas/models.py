from django.db import models
from django.core.exceptions import ValidationError

def validate_age(value):
    if value < 0 or value > 120:
        raise ValidationError('Edad debe estar entre 0 y 120.')
    
# Create your models here.
class Persona(models.Model):
    nombres = models.TextField(max_length = 100)
    apellidos = models.TextField(max_length = 100)
    edad = models.IntegerField(validators=[validate_age])
    donador = models.BooleanField()