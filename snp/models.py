from datetime import datetime
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    img = models.CharField(max_length=256, null=True, blank=True)
    date_time = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def like_count(self):
        return self.likes.count()
    
    def __str__(self):
        return self.text[:36]
    
    def get_absolute_url(self):
        return reverse('posts')
    
class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Track which user liked the post
    
    def __str__(self):
        return f"Like by {self.user.username} on {self.post.text[:20]}"
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.text[:30]}"

class Friend(models.Model):
    STATUS = ((1, "pending"), (2, "accepted"), (3, "rejected"), (4, "cancelled"), (5, "deleted"), )

    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="requests_sent", related_query_name="from_user")
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="requests_received", related_query_name="to_user")
    requested_at = models.DateTimeField(auto_now_add=True)
    friended_at = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        constraints =  [
            models.UniqueConstraint(fields=["from_user", "to_user"], name="unique_friend")
        ]

    def __str__(self):
        return f"{self.id} {self.from_user.username} friend with {self.to_user.username}"
