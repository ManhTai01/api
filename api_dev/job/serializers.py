from django.db import models
from rest_framework.serializers import ModelSerializer
from .models import Job


class JobSerializer(ModelSerializer):

    class Meta:
        model = Job
        fields = "__all__"
