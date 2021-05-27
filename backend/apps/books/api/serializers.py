from django.db import models
from django.db.models import fields
from rest_framework import serializers
# Models
from apps.books.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"
