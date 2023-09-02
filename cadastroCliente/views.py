from rest_framework import viewsets
from .models import Cadastro_Cliente, Genero
from .serializers import CadastroClienteSerializer, GeneroSerializer

# Create your views here.

class CadastroClienteViewSet(viewsets.ModelViewSet):
    queryset = Cadastro_Cliente.objects.all()
    serializer_class = CadastroClienteSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer