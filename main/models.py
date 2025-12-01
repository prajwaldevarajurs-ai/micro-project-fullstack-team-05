
from django.db import models
from django.contrib.auth.models import User

class Exam(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    room = models.CharField(max_length=20)
    seat = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


