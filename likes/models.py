from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    account_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    made_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-made_at']
        unique_together = ['account_owner', 'post']

    def __str__(self):
        return f'{self.account_owner} {self.post}'