from datetime import datetime
from django.conf import settings
from django.urls import reverse
from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    img = models.CharField(max_length=256)
    date_time = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.text[:36]
    
    def get_absolute_url(self):
        return reverse('posts')
    