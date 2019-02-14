from django.urls import path
from . import views

urlpatterns = [
   path('', views.blog, name='blog'),
   path('barang/tambah', views.input, name='input'),
   path('barang/<int:id>', views.blog_page, name='blog-page'),
]