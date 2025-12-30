from .models import Proyecto
from rest_framework import serializers, viewsets, permissions
from .serializers import ProyectoSerializer

# esta le dice al proyecto que consultas se podran hacer
# ModelViewSet es una clase que proporciona acciones predeterminadas para manejar solicitudes HTTP como GET, POST, PUT, DELETE
class ProyectoViewSet(viewsets.ModelViewSet): 
    queryset = Proyecto.objects.all() # conjunto de datos
    permission_classes = [permissions.AllowAny] # quien tiene permitido hacer operaciones, en este caso cualquiera
    serializer_class = ProyectoSerializer # le digo apartir de que serializer va a estar utilizando estos datos, es deicr, como se van a convertir los datos a json
    # http_method_names = ['get', 'post'] Me permite restringir los metodos HTTP que se pueden usar

# ok y si quiero crear una api para otro modelo, simplemente debo crear otro viewset en mi archivo api.py pero que se alimente de otro serializer que a su vez se alimenta de otro model de la base de datos,

# por ejemplo, si tuviera un modelo llamado Tarea, deberia crear un serializer llamado TareaSerializer y luego un viewset llamado TareaViewSet que use ese serializer y el modelo Tarea.
# Finalmente, deberia registrar ese nuevo viewset en el archivo urls.py para que las rutas de la API esten disponibles.
    