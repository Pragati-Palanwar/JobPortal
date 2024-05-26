from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_jobseeker, name='register_jobseeker'),
]
