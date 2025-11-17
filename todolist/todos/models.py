from django.db import models
from django.conf import settings



class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField()
    is_completed = models.BooleanField(default=False)
    due_date = models.DateField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def natural_key(self):
        return (self.title,) + self.owner.natural_key()

    def __str__(self):
        return self.title
