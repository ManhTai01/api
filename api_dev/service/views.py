from rest_framework.serializers import Serializer
from .models import Services
from django.db import models
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
