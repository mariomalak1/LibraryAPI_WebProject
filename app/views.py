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
        book = Book.objects.filter(ID=ref).first()
        if book:
            serializer = BookSerializer(book)
            return Response(serializer.data)
        else:
            return Response({"erorrs":"no book with this name."}, status=status.HTTP_404_NOT_FOUND)

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
                return Response({"category": "no category with this name."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"category": "category name field is required."}, status=status.HTTP_400_BAD_REQUEST)

        data = request.data.copy()
        data["category"] = category.pk

        serializer = NormalBookSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @staticmethod
    @api_view(["PATCH"])
    @is_admin
    def updateBook(request, ref, *args, **kwargs):
        data = request.data

        # get userBorrow and category if he need to update
        userBorrow = data.get("userBorrow")
        category = data.get("category")

        data = request.data.copy()

        if category:
            categoryObj = Category.objects.filter(name=category).first()
            if not categoryObj:
                return Response({"category": "no category with this name."}, status=status.HTTP_400_BAD_REQUEST)
            data["category"] = categoryObj.id

        if userBorrow:
            userBorrowObj = User.objects.filter(username=userBorrow).first()
            if not userBorrowObj:
                return Response({"userBorrow": "no user with this username."}, status=status.HTTP_400_BAD_REQUEST)
            data["userBorrow"] = userBorrowObj.id


        book = Book.objects.filter(ID=ref).first()
        if not book:
            return Response({"errors":"no book  with this name."}, status=status.HTTP_404_NOT_FOUND)

        serializer = NormalBookSerializer(data=data, instance=book, partial=True)
        if serializer.is_valid():
            book = serializer.update(instance=book, validated_data=serializer.validated_data)
            serializer2 = BookSerializer(book)
            return Response(serializer2.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @staticmethod
    @api_view(["DELETE"])
    @is_admin
    def deleteBook(request, ref, *args, **kwargs):
        book = Book.objects.filter(ID=ref).first()
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

    @staticmethod
    @api_view(["POST"])
    @isAuthenticatedWithValidToken
    def borrowBook(request, ref, *args, **kwargs):
        token = kwargs.get("token")
        book = Book.objects.filter(ID=ref).first()
        if not book:
            return Response({"errors":"no book with this name."}, status=status.HTTP_404_NOT_FOUND)
        if not book.avaliable:
            return Response({"errors":"this book not avaliable now."}, status=status.HTTP_400_BAD_REQUEST)

        book.avaliable = False
        book.userBorrow = token.user
        book.save()
        return Response({"success":"book borrowed successfully"}, status=status.HTTP_200_OK)

    @staticmethod
    @api_view(["POST"])
    @isAuthenticatedWithValidToken
    def returnBookBack(request, ref, *args, **kwargs):
        token = kwargs.get("token")
        book = Book.objects.filter(ID=ref).first()
        if not book:
            return Response({"errors": "no book with this name."}, status=status.HTTP_404_NOT_FOUND)
        if book.userBorrow != token.user:
            return Response({"errors": "you don't borrow this book before."}, status=status.HTTP_400_BAD_REQUEST)

        book.avaliable = True
        book.userBorrow = None
        book.save()
        return Response({"success": "book returned successfully"}, status=status.HTTP_200_OK)
