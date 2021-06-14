from django.shortcuts import render
from .models import Job
from .serializers import JobSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
