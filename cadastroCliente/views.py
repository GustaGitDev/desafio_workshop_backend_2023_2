from rest_framework import viewsets, filters
from .models import Cadastro_Cliente, Genero
from .serializers import CadastroClienteSerializer, GeneroSerializer
from .pagination import PaginaCustomizadaGeneros, PaginaCustomizadaUsuarios

# Create your views here.

class CadastroClienteViewSet(viewsets.ModelViewSet):
    queryset = Cadastro_Cliente.objects.all()
    serializer_class = CadastroClienteSerializer
    pagination_class = PaginaCustomizadaUsuarios
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'email', 'numero', 'Genero__sexo']


class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    pagination_class = PaginaCustomizadaGeneros
