from rest_framework.pagination import PageNumberPagination

class YorumPagination(PageNumberPagination):
    page_size = 5