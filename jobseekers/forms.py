from django import forms
from .models import JobSeeker

class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        fields = ['resume', 'skills', 'experience', 'looking_for_remote', 'looking_for_flexible_hours']
