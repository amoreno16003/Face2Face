from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Chatroom(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(Participant, blank=True)
    
    def __str__(self):
        return self.name
    
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Video_Chat(models.Model):
    participants = models.ManyToManyField(Participant)
    date = models.DateTimeField(auto_now_add=True)