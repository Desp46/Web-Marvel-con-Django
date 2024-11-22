from django.db import models

# Create your models here.
class marvel(models.Model):
    nombre=models.CharField(max_length=200)
    nombre_real=models.CharField(max_length=100, blank=False, null=False, default="Desconocido")
    peso=models.IntegerField()
    altura=models.FloatField()
    descripcion=models.CharField(max_length=500, blank=False, null=False, default="Desconocido")
    imagen= models.FileField(upload_to="marvel/")
    
    def __str__(self):
        return self.nombre