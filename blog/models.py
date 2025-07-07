from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class Category(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    post_time = models.DateTimeField(auto_now=True)
    modified_time = models.DateTimeField(default=timezone.now())
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.title

