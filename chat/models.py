from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, related_name='messages_sent', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='messages_received', on_delete=models.CASCADE)