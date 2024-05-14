from rest_framework import serializers
from .models import *

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

class ResultadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultados
        fields = '__all__'

class PruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prueba
        fields = '__all__'

class ConfirmacionRiesgosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Confirmacion_riesgos
        fields = '__all__'

class EPPsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EPPs
        fields = '__all__'

class EPpListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EPp_Lista
        fields = '__all__'
