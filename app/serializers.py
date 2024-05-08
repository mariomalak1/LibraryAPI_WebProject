from rest_framework import serializers

from Authentication.serializer import UserSerializer

from .models import Category, Book

# create serializers here

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]

class BookSerializer(serializers.ModelSerializer):
    # category = serializers.SerializerMethodField()
    avaliable = serializers.BooleanField(default=True)
    class Meta:
        model = Book
        fields = ["bookName", "authorName", "avaliable", "description", "category", "userBorrow"]

    # def get_category(self, obj):
    #     categorySerializer = CategorySerializer(obj.category)
    #     return categorySerializer.data


