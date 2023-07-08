from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=200, unique=True)
    discord = models.CharField(max_length=200, unique=True)
    games = models.CharField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    # Add Time Zone and Times

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="game_events"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    event_date = models.DateTimeField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-event_date"]

    def __str__(self):
        return self.title
