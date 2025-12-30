# conecta tus ViewSets con las URLs reales que el navegador o el frontend puede consumir

from rest_framework import routers
from .api import ProyectoViewSet

router = routers.DefaultRouter() # crea un enrutador predeterminado para manejar las rutas de la API
router.register(r'api/proyectos', ProyectoViewSet, 'proyectos') # registra el ViewSet de Proyecto con la ruta 'api/proyectos'

urlpatterns = router.urls # asigna las URLs generadas por el enrutador a urlpatterns