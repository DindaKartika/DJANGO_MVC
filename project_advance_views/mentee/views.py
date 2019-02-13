from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Mentee

def mentee(request):
    mentee = Mentee.objects.all()
    return render(request, 'ATA/mentee.html', {'mentees':mentee})
