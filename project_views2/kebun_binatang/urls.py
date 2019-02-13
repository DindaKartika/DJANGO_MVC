from django.urls import path
from . import views

urlpatterns = [
   path('', views.input_post, name='daftar_binatang'),
   path('db_binatang', views.db_binatang, name='db_binatang'),
   path('base_binatang', views.base_binatang, name='base_binatang'),
]