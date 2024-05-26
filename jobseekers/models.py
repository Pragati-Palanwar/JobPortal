
from django.db import models
from django.contrib.auth.models import User

class JobSeeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    skills = models.TextField()
    experience = models.IntegerField()
    looking_for_remote = models.BooleanField(default=False)
    looking_for_flexible_hours = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
