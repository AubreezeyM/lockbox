from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class Post(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100000)
    post_time = models.DateTimeField(auto_now=True)
    modified_time = models.DateTimeField(default=timezone.now())