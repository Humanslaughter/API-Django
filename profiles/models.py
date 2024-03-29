from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    image = models.ImageField(upload_to='images/', default='../default_profile_ftyuqx')
    account_owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    made_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-made_at']

    def __str__(self):
        return f"{self.account_owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(account_owner=instance)

post_save.connect(create_profile, sender=User)
