from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now(), blank=True)
    
    def __str__(self):
        return self.title