from django.db import models

class Book(models.Model):
    Title = models.CharField(max_length=100)
    Description=models.CharField(max_length=100)
    Author=models.CharField(max_length=100)
    Created_at=models.DateTimeField(auto_now_add=True)
