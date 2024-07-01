

# Create your models here.
# quotes_consumer/models.py

from django.db import models

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.text  # Example representation method
