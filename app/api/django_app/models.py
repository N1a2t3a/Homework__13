from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
  