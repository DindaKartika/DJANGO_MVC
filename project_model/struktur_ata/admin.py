from django.contrib import admin
from django.contrib import admin
from .models import Direksi, Mentee, MataPelajaran, Mentor, Challenge, LiveCode

# Register your models here.

my_model = [Direksi, Mentee, MataPelajaran, Mentor, Challenge, LiveCode]
admin.site.register(my_model)