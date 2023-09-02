from rest_framework import pagination

class PaginaCustomizadaUsuarios(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'count'
    max_page_size = 5
    page_query_param = 'p'

class PaginaCustomizadaGeneros(pagination.PageNumberPagination):
    page_size = 3
    page_size_query_param = 'count'
    max_page_size = 5
    page_query_param = 'p'
