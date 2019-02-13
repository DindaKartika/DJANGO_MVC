from django.urls import path
from . import views

urlpatterns = [
   path('blog', views.blog, name='blog'),
   path('input', views.input, name='input'),
   path('blog/<int:id>', views.blog_page, name='blog-page'),
]