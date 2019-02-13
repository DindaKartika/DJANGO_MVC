from django.shortcuts import render, redirect
from django.utils import timezone
from .models import BlogPost
from .forms import PostForm

# Create your views here.
def blog(request):
    post = BlogPost.objects.all()
    return render(request, 'ATA/blog.html', {'posts':post})

def input(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog')
    else:
        form = PostForm()
    return render(request, 'ATA/input.html', {'form':form})