from django.db import models

# Create your models here.
class Project(models.Model):
    titulo = models.CharField(max_length = 50)
    descripcion =  models.TextField(blank = True)
    tecnologia = models.CharField(max_length = 50)
    creacion = models.DateTimeField(auto_now_add = True)

