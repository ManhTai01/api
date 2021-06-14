from django.shortcuts import render
from .models import Talent
from .serializers import TalentSerializer
from rest_framework.response import Response
from rest_framework import viewsets


class TalentViewSet(viewsets.ModelViewSet):
    queryset = Talent.objects.all()
    serializer_class = TalentSerializer
