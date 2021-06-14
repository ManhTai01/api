from typing import AsyncIterator
from django.contrib import admin
from .models import SubmissionJob
from django.utils.safestring import mark_safe
# Register your models here.


class SubmissionJobAdmin(admin.ModelAdmin):
    list_display = ['file_review', 'email', 'first_name', 'last_name', 'phone']

    actions = ['file_review']

    def file_review(self, obj):
        if obj.file:
            return mark_safe('<a href="{0}" target="_blank"><p>{1}</p></a>'.format(obj.file.url, obj.file))
        else:
            return '-'

    file_review.short_description = 'File'
    file_review.allowed = True


admin.site.register(SubmissionJob, SubmissionJobAdmin)
