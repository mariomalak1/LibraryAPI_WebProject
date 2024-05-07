import datetime

from django.contrib.auth import authenticate, login, logout

from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from rest_framework import status
from rest_framework.authtoken.models import Token

from .models import User, ResetCode
from .serializer import RegisterSerializer, ForgetPassword,\
    UserSerializer, ResetCodeSerializer, ResetPasswordSerializer, SignInSerializer, UpdateUserPassword
from .utils import resetPasswordSendMail
from project.utilis import getDataFromPaginator
# Create your views here.


class UserAuthentication:
    @staticmethod
    def get_token_or_none(request):
        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        if not authorization_header:
            authorization_header = request.data.get("token")
            if not authorization_header:
                return None
        try:
            # Split the header value to extract the token
            auth_type, token = authorization_header.split(' ')
        except:
            token = authorization_header

        if token:
            token_ = Token.objects.filter(key=token).first()
            if token_:
                return token_

        return None

    @staticmethod
    @api_view(["GET"])
    def token_check_found(request):
        token_ = UserAuthentication.get_token_or_none(request)
        if token_ is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        token_required = Token.objects.filter(key=token_).first()
        if token_required:
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    @api_view(["GET"])
    def login(request):
        serializer = SignInSerializer(data = request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            user = User.objects.filter(email=username).first()
            if user:
                user = authenticate(request, username=user.username, password=serializer.validated_data.get("password"))
                if user:
                    login(request, user)
                    token = Token.objects.filter(user=user).first()
                    if not token:
                        token = Token.objects.create(user=user)
                else:
                    return Response({"message":"invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)
                return Response({"message": "user login succssfully", "token":token.key}, status=status.HTTP_200_OK)
            else:
                return Response({"errors":"no user with this username"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @api_view(["POST"])
    def signup(request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            user = User.objects.filter(username=serializer.data.get("username")).first()
            if user:
                return Response({"error": "this username is already register"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            if serializer.data.get("rePassword") == serializer.data.get("password"):
                user = User(username=serializer.data.get("username"))
                user.set_password(serializer.data.get("password"))
                user.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"errors":"password not match"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)