from django.db import models
from django.contrib.auth.models import User

class Reflection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reflection by {self.user.username} on {self.created_at.strftime('%Y-%m-%d')}"
