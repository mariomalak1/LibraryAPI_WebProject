from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status

from .models import *
from .serializers import *

# Create your views here.

class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookView(APIView):
    def get(self, request):
        data = request.data
        if data.get("name"):
            books = Book.objects.filter(bookName__icontains=data.get("name"))
        else:
            books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def get_object(self, request, ref):
        book = Book.objects.filter(bookName=ref).first()
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def post(self, request):
        pass