from django.db import models


class SubmissionJob(models.Model):
    file = models.FileField(upload_to="file/")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ['-id']
        db_table = 'jobSubmission'
