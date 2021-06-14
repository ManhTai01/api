from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250, null=False)
    content = models.TextField(blank=True, null=False)
    summary = models.CharField(max_length=250)
    thumnail = models.ImageField(upload_to='blog', blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey('users.User', related_name='author', on_delete=models.CASCADE, null=True)
    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'blog'
        ordering = ['-id']
