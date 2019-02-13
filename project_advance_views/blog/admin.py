from django.contrib import admin
from django.contrib import admin
from .models import BlogPost

# Register your models here.

my_model = [BlogPost]
admin.site.register(my_model)