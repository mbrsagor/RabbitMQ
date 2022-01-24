from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=70)
    details = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title[:30]
