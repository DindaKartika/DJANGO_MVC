from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import ImageField
from django.utils import timezone

# Create your models here.
class BlogPost(models.Model):
    nama = models.CharField(max_length = 255)
    gambar = models.ImageField(max_length = 255, default="")
    harga = models.CharField(max_length = 1000)
    keterangan = models.TextField(max_length = 25, default="0")
    tanggal = models.DateField(default = timezone.now)