from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import *
from .serializers import *
from .decorators import is_admin, isAuthenticatedWithValidToken

# Create your views here.

class CategoryView:
    @staticmethod
    @api_view(["GET"])
    @is_admin
    def getAllCategories(request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    @staticmethod
    @api_view(["POST"])
    @is_admin
    def postCategory(request, *args, **kwargs):
        data = request.data
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookView:
    @staticmethod
    @api_view(["GET"])
    @isAuthenticatedWithValidToken
    def getAllBooks(request, *args, **kwargs):
        data = request.data

        books = Book.objects.all()

        # do search filter

        if data.get("name"):
            books = books.objects.filter(bookName__icontains=data.get("name")).all()

        elif data.get("author"):
            books = books.objects.filter(authorName__icontains=data.get("author")).all()

        elif data.get("category"):
            books = books.objects.filter(category__name__icontains=data.get("category")).all()

        elif data.get("is_avalible_only"):
            books = books.filter(avalible=True).all()

        elif data.get("avaliable_not_borrow"):
            books = books.filter(avalible=True).all()

        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    @staticmethod
    @api_view(["GET"])
    @isAuthenticatedWithValidToken
    def getBook(request, ref, *args, **kwargs):
        book = Book.objects.filter(bookName=ref).first()
        serializer = BookSerializer(book)
        return Response(serializer.data)

    @staticmethod
    @api_view(["POST"])
    @is_admin
    def createBook(request, *args, **kwargs):
        data = request.data

        # try to check that category is created before
        categoryName = data.get("category")
        if categoryName:
            category = Category.objects.filter(name=categoryName).first()
            if not category:
                return Response({"errors": "no category with this name."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"errors": "category name field is required."}, status=status.HTTP_400_BAD_REQUEST)

        data = request.data.copy()
        data["category"] = category.pk

        print(data["category"])

        serializer = BookSerializer(data=data)

        if serializer.is_valid():
            book = serializer.save()
            print(serializer.validated_data.get("avaliable"))
            if ((serializer.validated_data.get("avaliable")) or (serializer.validated_data.get("avaliable") is None)):
                book.avaliable = True
                book.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @staticmethod
    @api_view(["PATCH"])
    @is_admin
    def patch(request, ref, *args, **kwargs):
        data = request.data
        serializer = BookSerializer(data=data, instance=subject, partial=True)
        # if serializer.is_valid()


    @staticmethod
    @api_view(["DELETE"])
    @is_admin
    def delete(request, ref, *args, **kwargs):
        book = Book.objects.filter(bookName=ref).first()
        if not book:
            return Response({"errors":"no book with this name."}, status=status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response({"success":"book deleted successfully."}, status=status.HTTP_200_OK)

class BorrowBookView:
    @staticmethod
    @api_view(["GET"])
    @isAuthenticatedWithValidToken
    def getAllBorrowedBooksByUser(request, *args, **kwargs):
        token = kwargs.get("token")
        books = Book.objects.filter(userBorrow_id=token.user.id).all()

        serializer = BookSerializer(books, many=True)

        return Response(serializer.data)
