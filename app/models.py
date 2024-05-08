from django.db import models
from django.contrib.auth.models import User as djangoUser
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    bookName = models.CharField(max_length=150, null=False, blank=False, unique=True)
    authorName = models.CharField(max_length=150, null=False, blank=False)

    avaliable = models.BooleanField(default=True)

    # user that borrow book
    userBorrow = models.ForeignKey(djangoUser, on_delete=models.SET_NULL, null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['bookName', "authorName", "category__name"]

