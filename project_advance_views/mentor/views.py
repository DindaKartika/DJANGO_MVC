from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Mentor

def mentor(request):
    mentor = Mentor.objects.all()
    return render(request, 'ATA/mentor.html', {'mentors':mentor})
