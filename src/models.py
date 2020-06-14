from django.db import models
from django.utils.timezone import datetime


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255, editable=True)
    isbn_number = models.CharField(max_length=15, editable=True)
    book_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
