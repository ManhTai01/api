from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Services


class ServiceSerializer(ModelSerializer):

    class Meta:
        model = Services
        fields = '__all__'
