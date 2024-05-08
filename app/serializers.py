from rest_framework import serializers

from Authentication.serializer import UserSerializer

from .models import Category, Book

# create serializers here

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]

class BookSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ["bookName", "authorName", "avalibleNumber", "description", "category", "userBorrow"]

    def get_category(self, obj):
        categorySerializer = CategorySerializer(obj.category)
        return categorySerializer.data


