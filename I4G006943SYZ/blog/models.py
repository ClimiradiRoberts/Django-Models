from turtle import title
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=200)
    author = models.CharField(max_length=23)
    created_date = models.DateTimeField
    Published_date = models.DateTimeField