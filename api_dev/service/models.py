from django.db import models
from django.db.models.base import Model


class Services(models.Model):
    image = models.ImageField(help_text="1:1", upload_to='service')
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        db_table = 'service'
