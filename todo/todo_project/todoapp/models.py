from django.db import models

# Create your models here.


class Task(models.Model):
    
    taskname=models.CharField(max_length=100)
    is_completed=models.BooleanField(default=False)
    
    created_at=models