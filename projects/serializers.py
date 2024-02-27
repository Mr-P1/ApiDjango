from rest_framework import serializers
from .models import * 

class Projectserializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id','titulo','descripcion','tecnologia','creacion']
        read_only_fields = ('creacion',  ) # No se podra modificar ni eliminar, debe ir la coma por que lo lee como una tupla

