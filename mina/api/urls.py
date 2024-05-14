from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'usuarios', UsuariosViewSet)
router.register(r'resultados', ResultadosViewSet)
router.register(r'pruebas', PruebaViewSet)
router.register(r'confirmacion-riesgos', ConfirmacionRiesgosViewSet)
router.register(r'epps', EPPsViewSet)
router.register(r'epp-lista', EPpListaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
