from django.urls import path

from .views import *

urlpatterns = [
    path("categories/", CategoryView.getAllCategories, name="getAllCategories"),
    path("category/", CategoryView.postCategory, name="postCategory"),


    path("createBook/", BookView.createBook, name="createBook"),
    path("getAllbooks/", BookView.getAllBooks, name="getAllBooks"),
    path("getBook/<ref>/", BookView.getBook, name="getBook"),
    path("deleteBook/<ref>", BookView.deleteBook, name="deleteBook"),
    path("updateBook/<ref>", BookView.updateBook, name="updateBook"),

    path("getAllBorrowedBooksByUser/",
         BorrowBookView.getAllBorrowedBooksByUser, name="getAllBorrowedBooksByUser"),
    path("borrowBook/<ref>/",
         BorrowBookView.borrowBook, name="borrowBook"),
    path("returnBookBack/<ref>/",
         BorrowBookView.returnBookBack, name="returnBookBack"),

]