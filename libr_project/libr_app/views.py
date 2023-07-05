from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


class BookCreateList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class=BookSerializer


