from django.db import models

# Create your models here.
class Todo(models.Model):
    item = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item