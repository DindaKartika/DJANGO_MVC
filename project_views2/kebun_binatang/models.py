from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from django.utils import timezone

# Create your models here.
class Hewan(models.Model):
    nama = models.CharField(max_length = 255)
    species = models.CharField(max_length = 100)
    berat = models.CharField(max_length = 5)
    umur = models.CharField(max_length = 5)

class Kandang(models.Model):
    nama = models.CharField(max_length = 255)
    isi_kandang = models.CharField(max_length = 10)
    luas_kandang = models.CharField(max_length = 25)

class Penjaga(models.Model):
    nama = models.CharField(max_length = 255)
    telepon = models.CharField(max_length = 25)
    jadwal_jaga = models.DateTimeField()

class Pengunjung(models.Model):
    nama = models.CharField(max_length = 255)
    telepon = models.CharField(max_length = 25)
    hari_kunjung = models.DateTimeField(default=timezone.now)