from django.db import models

# Create your models here.
class Persona(models.Model):
    nombres = models.TextField(max_length = 100)
    apellidos = models.TextField(max_length = 100)
    edad = models.TextField() # (max_digits = 3)