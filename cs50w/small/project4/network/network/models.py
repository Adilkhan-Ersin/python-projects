from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    content = models.CharField(max_length=140)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userPost")
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def __str__(self):
        return f"Post by {self.user} at {self.created_at.strftime('%d %b %Y %H:%M')}"
    def like_count(self):
        return self.likes.count()
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userLike")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="postLike")

    def __str__(self):
        return f"Like by {self.user} on {self.post}"
    
class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userFollow")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userFollowing")

    def __str__(self):
        return f"{self.follower} follows {self.following}"
    
