from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User

from Authentication.views import UserAuthentication

def isAuthenticatedWithValidToken(func):
    def test_user(request, *args, **kwargs):
        token = UserAuthentication.get_token_or_none(request)
        if token:
            return func(request, *args, **kwargs)
        else:
            return Response({"errors": "you must login first."},
                            status=status.HTTP_403_FORBIDDEN)
    return test_user


def is_admin(func):
    def test_user(request, *args, **kwargs):
        token = UserAuthentication.get_token_or_none(request)
        if not token:
            return Response({"errors": "you must login first."},
                            status=status.HTTP_403_FORBIDDEN)
        elif token.user.is_staff:
            return func(request, *args, **kwargs)
        else:
            return Response({"errors": "you not authorized to enter this page."},
                            status=status.HTTP_403_FORBIDDEN)
    return test_user
