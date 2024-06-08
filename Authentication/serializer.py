from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password", "confirmPassword", "is_admin"]

    confirmPassword = serializers.CharField(required=True)
    is_admin = serializers.BooleanField(default=False)

    def create(self, validated_data):
        self.instance.is_staff = validated_data.get("is_admin")
        self.instance.set_password(validated_data.get("password"))

        return super().create(self, validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "is_staff"]

    def is_valid(self, raise_exception=False):
        if self.partial:
            self.fields.get("email").validators = []
        return super().is_valid(raise_exception=raise_exception)

