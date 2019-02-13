from django.shortcuts import render

# Create your views here.
def mentee(request):
   return render(request, 'ATA/mentee.html', {})