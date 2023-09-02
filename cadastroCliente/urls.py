from rest_framework import routers
from .views import CadastroClienteViewSet, GeneroViewSet

router = routers.DefaultRouter()
router.register(r'CadastroCliente', CadastroClienteViewSet)
router.register(r'Genero', GeneroViewSet)
urlpatterns = router.urls