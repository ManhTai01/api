from django.utils import timezone
from django.db import models


# Create your models here.


class Talent(models.Model):
    name = models.CharField(max_length=250, null=False)
    dateOfBirth = models.DateTimeField(default=timezone.now)
    phone = models.CharField(max_length=12, null=False)
    regency = models.CharField(max_length=250, null=False)
    avt = models.ImageField(help_text="1:1", upload_to='talent')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        db_table = 'talent'
