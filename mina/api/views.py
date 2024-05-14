from rest_framework import viewsets
from .models import *
from .serializers import *

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class ResultadosViewSet(viewsets.ModelViewSet):
    queryset = Resultados.objects.all()
    serializer_class = ResultadosSerializer

class PruebaViewSet(viewsets.ModelViewSet):
    queryset = Prueba.objects.all()
    serializer_class = PruebaSerializer

class ConfirmacionRiesgosViewSet(viewsets.ModelViewSet):
    queryset = Confirmacion_riesgos.objects.all()
    serializer_class = ConfirmacionRiesgosSerializer

class EPPsViewSet(viewsets.ModelViewSet):
    queryset = EPPs.objects.all()
    serializer_class = EPPsSerializer

class EPpListaViewSet(viewsets.ModelViewSet):
    queryset = EPp_Lista.objects.all()
    serializer_class = EPpListaSerializer
