from django.contrib import admin
from django.contrib import admin
from .models import Post, Mentee

# Register your models here.

my_model = [Post, Mentee]
admin.site.register(my_model)