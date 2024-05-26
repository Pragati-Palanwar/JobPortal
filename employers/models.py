from django.db import models
from django.contrib.auth.models import User

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, default="developer")
    job_openings = models.IntegerField()
    accepts_remote = models.BooleanField(default=False)
    flexible_hours = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name
