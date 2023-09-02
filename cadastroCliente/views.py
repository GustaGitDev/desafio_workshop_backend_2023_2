from rest_framework import viewsets
from .models import Cadastro_Cliente, Genero
from .serializers import CadastroClienteSerializer, GeneroSerializer
from .pagination import PaginaCustomizadaGeneros, PaginaCustomizadaUsuarios

# Create your views here.

class CadastroClienteViewSet(viewsets.ModelViewSet):
    queryset = Cadastro_Cliente.objects.all()
    serializer_class = CadastroClienteSerializer
    pagination_class = PaginaCustomizadaUsuarios

    def get_queryset(self):

        txt_nome = self.request.GET.get('nome')

        if txt_nome:
            nome = Cadastro_Cliente.objects.filter(nome__icontains=txt_nome)
        else:
            nome = Cadastro_Cliente.objects.all()

        return nome

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    pagination_class = PaginaCustomizadaGeneros
