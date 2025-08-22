from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre  = models.CharField(max_length=100)
    descripcion = models.TextField()
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='proyectos/',blank=True, null=True)


    