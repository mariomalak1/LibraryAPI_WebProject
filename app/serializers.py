from rest_framework import serializers

from django.contrib.auth.models import User

from Authentication.serializer import UserSerializer

from .models import Category, Book
# create serializers here

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]

class BookSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    userBorrow = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ["bookName", "authorName", "avaliable", "description", "category", "userBorrow"]

    def get_category(self, obj):
        categorySerializer = CategorySerializer(obj.category)
        return categorySerializer.data

    def get_userBorrow(self, obj):
        if obj.userBorrow:
            userSerializer = UserSerializer(obj.userBorrow)
            return userSerializer.data
        return None


class NormalBookSerializer(serializers.ModelSerializer):
    avaliable = serializers.BooleanField(default=True)

    class Meta:
        model = Book
        exclude = ["id"]

    def update(self, instance, validated_data):
        newInstace = super().update(instance, validated_data)
        if newInstace.userBorrow is None:
            newInstace.avaliable = True
            newInstace.save()
        elif newInstace.userBorrow:
            newInstace.avaliable = False
            newInstace.save()
        return newInstace
