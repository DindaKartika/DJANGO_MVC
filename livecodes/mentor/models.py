from django.db import models
from django.db.models import CharField
from django.db.models import TextField

# Create your models here.

class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length = 255)
    nick_name = models.CharField(max_length = 255, default = "")
    experience = models.CharField(max_length=2)
    image = models.CharField(max_length = 255, default = "")
    kesan = models.TextField(max_length = 255, default = "")