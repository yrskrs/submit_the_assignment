from django.db import models

# Create your models here.

from django.utils import timezone

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(default=timezone.now)

class UploadedLink(models.Model):
    link = models.URLField()
    uploaded_at = models.DateTimeField(default=timezone.now)
