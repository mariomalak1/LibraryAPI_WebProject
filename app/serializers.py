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

    # def is_valid(self, raise_exception=False):
    #     if self.partial:
    #         print(self.fields["userBorrow"])
    #         self.fields["userBorrow"] =
    #         print(self.fields.get("category"))
    #         print(self.fields.get("category").validators)
    #         # print(help(self.fields.get("category")))
    #         self.fields.get("category").validators = []
    #     return super().is_valid(raise_exception=raise_exception)

    def update(self, instance, validated_data):
        newInstace = super().update(instance, validated_data)
        if newInstace.userBorrow is None:
            newInstace.avaliable = True
            newInstace.save()
        elif newInstace.userBorrow:
            newInstace.avaliable = False
            newInstace.save()
        return newInstace
