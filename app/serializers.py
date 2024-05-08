from rest_framework import serializers

from .models import Category, Book
from Authentication.serializer import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]

class BookSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ["bookName", "authorName", "avalibleNumber", "description", "category"]

    def get_category(self, obj):
        categorySerializer = CategorySerializer(obj.category)
        return categorySerializer.data

class BorrowBookSerizlizer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = BorrowBook
        fields = ["book", "user"]

    def get_book(self, obj):
        bookSerializer = BookSerializer(obj.book)
        return bookSerializer.data

    def get_user(self, obj):
        userSerializer = UserSerializer(obj.user)
        return userSerializer.data

