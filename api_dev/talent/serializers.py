from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Talent


class TalentSerializer(ModelSerializer):

    class Meta:
        model = Talent
        fields = "__all__"
