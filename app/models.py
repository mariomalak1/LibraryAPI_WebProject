from django.db import models
from django.contrib.auth.models import User as djangoUser
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=70)


class Book(models.Model):
    bookName = models.CharField(max_length=150, null=False, blank=False)
    authorName = models.CharField(max_length=150, null=False, blank=False)
    avalibleNumber = models.PositiveSmallIntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)


    class Meta:
        ordering = ['bookName', "authorName", "category_name"]

class BorrowBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(djangoUser, on_delete=models.CASCADE)


