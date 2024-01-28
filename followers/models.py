from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    followed = models.ForeignKey(User, related_name='followed', on_delete=models.CASCADE)
    account_owner = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    made_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-made_at']
        unique_together = ['account_owner', 'followed']

    def __str__(self):
        return f'{self.account_owner} {self.followed}'