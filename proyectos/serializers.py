from rest_framework import serializers
from .models import Proyecto

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ['id', 'titulo', 'descripcion', 'tecnologia', 'fecha_creacion'] # campos que quiero exponer a traves del API
        read_only_fields = ['fecha_creacion'] # digo que este campo es solo de lectura