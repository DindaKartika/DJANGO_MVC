from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Hewan
from .forms import AnimalForm

def input_post(request):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('db_binatang')
    else:
        form = AnimalForm()
    return render(request, 'binatang/daftar_binatang.html', {'form':form})

# Create your views here.
# def daftar_binatang(request):
#     return render(request, 'binatang/daftar_binatang.html', {})

def db_binatang(request):
    binatang = Hewan.objects.all()
    return render(request, 'binatang/db_binatang.html', {'binatangs':binatang})

def base_binatang(request):
    binatang = Hewan.objects.all()
    return render(request, 'binatang/base_binatang.html', {'binatangs':binatang})