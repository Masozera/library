from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    isbn = models.CharField(max_length=12)

    def __str__(self):
        return self.title
        
