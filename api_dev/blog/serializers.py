from django.db import models
from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.CharField(max_length=250)

    class Meta:
        model = Blog
        fields = "__all__"
