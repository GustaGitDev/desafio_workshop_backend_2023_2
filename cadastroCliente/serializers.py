from rest_framework import serializers
from .models import Cadastro_Cliente, Genero

class CadastroClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cadastro_Cliente
        fields = '__all__'

class GeneroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genero
        fields = '__all__'