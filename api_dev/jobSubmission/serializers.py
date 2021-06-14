# from typing_extensions import Required
from django.db import models
from rest_framework import serializers
from .models import SubmissionJob


class SubSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(max_length=11)

    class Meta:
        model = SubmissionJob
        fields = ['first_name', 'last_name', 'email', 'phone', 'file']
        ordering = ['-id']


class EmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    name = serializers.CharField()
    phone = serializers.CharField()
    content = serializers.CharField()

    class Meta:
        fields = ['email', 'name', 'phone', 'content']
        model = SubmissionJob
