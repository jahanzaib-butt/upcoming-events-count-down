from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    description = models.TextField()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.name