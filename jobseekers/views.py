
from django.shortcuts import render, redirect
from .forms import JobSeekerForm

def register_jobseeker(request):
    if request.method == 'POST':
        form = JobSeekerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobSeekerForm()
    return render(request, 'jobseekers/register.html', {'form': form})
