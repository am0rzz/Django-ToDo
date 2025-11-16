from django.db import models

# Create your models here.

class todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    due_date = models.DateField()
