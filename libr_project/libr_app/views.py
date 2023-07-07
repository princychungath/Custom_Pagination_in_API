from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from .pagination import MyCustomPagination



class BookCreateList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class=MyCustomPagination


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class=BookSerializer


