from django.shortcuts import render, redirect
from .forms import EmployerForm

def register_employer(request):
    if request.method == 'POST':
        form = EmployerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployerForm()
    return render(request, 'employers/register.html', {'form': form})
