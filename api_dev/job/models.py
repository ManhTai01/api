from django.db import models
from django.utils import timezone


class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    location = models.CharField(max_length=255, help_text="Company location")
    vacancies = models.IntegerField(default=1)
    content = models.TextField(blank=True, null=False, help_text="Job introductions")
    image = models.ImageField(upload_to='jobDescription/', help_text="Image logo company")
    urgent = models.BooleanField(default=True)
    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        db_table = 'job'
