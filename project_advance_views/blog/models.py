from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import ImageField
from django.utils import timezone

# Create your models here.
class BlogPost(models.Model):
    judul = models.CharField(max_length = 255)
    image = models.ImageField(max_length = 255, default="")
    konten = models.TextField(max_length = 1000)
    tanggal = models.DateField(default = timezone.now)
    comment = models.CharField(max_length = 25)