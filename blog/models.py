from django.db import models

# Create your models here.
class Post(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title