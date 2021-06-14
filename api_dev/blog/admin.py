from django.contrib import admin

# Register your models here.
from django.db import models
from .models import Blog
# Register your models here.


class BlogAmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'thumnail', 'create_at']


admin.site.register(Blog, BlogAmin)
