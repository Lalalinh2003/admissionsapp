from rest_framework.pagination import PageNumberPagination


class InformationPagination(PageNumberPagination):
    page_size = 10


class QuestionPagination(PageNumberPagination):
    page_size = 25