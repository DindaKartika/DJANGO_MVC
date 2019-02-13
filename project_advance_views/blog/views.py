from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Hewan
from .forms import AnimalForm

# Create your views here.
def blog(request):
   return render(request, 'blog/blog.html', {})

def input_post(request):
    if request.method == "POST":
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog')
    else:
        form = BlogForm()
    return render(request, 'ATA/input.html', {'form':form})