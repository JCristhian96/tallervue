from rest_framework import viewsets
# Serializers
from apps.books.api.serializers import BookSerializer
# Models
from apps.books.models import Book


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer