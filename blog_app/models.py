from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
