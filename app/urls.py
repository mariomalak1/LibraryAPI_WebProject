from django.urls import path

from .views import *

urlpatterns = [
    path("categories/", CategoryView.getAllCategories, name="getAllCategories"),
    path("category/", CategoryView.postCategory, name="postCategory"),


    # path("books/", BookView.get, name="bookViews"),
    path("books/", BookView.createBook, name="createBook"),

    path("getAllBorrowedBooksByUser/",
         BorrowBookView.getAllBorrowedBooksByUser, name="getAllBorrowedBooksByUser"),

]