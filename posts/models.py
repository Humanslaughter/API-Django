from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    image_filter_choices = [
        ('_1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
    ]
    account_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default='../default_post_hde9ti', blank=True)
    image_filter = models.CharField(max_length=32, choices=image_filter_choices, default='normal')
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    made_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-made_at']

    def __str__(self):
        return f'{self.id} {self.title}'