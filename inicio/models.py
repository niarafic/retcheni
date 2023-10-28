from django.db import models

# Create your models here.
class Miembros(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    mail=models.CharField(max_length=30)
    def __str__(self):
        return f'{self.id} - {self.nombre}-{self.apellido}-{self.mail}'


    
    