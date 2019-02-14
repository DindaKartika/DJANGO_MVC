from django.db import models
from django.db.models import CharField
from django.db.models import TextField

# Create your models here.
class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length = 255)
    foto = models.CharField(max_length = 255)
    kesan = models.TextField(max_length = 255)