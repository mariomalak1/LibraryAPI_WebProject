from django.urls import path, include

urlpatterns = [
    path("auth/", include("Authentication.urls")),
    path("app/", include("app.urls")),
]