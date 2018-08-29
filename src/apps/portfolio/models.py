from django.utils import timezone
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now(), blank=True)
    
    def __str__(self):
        return self.title