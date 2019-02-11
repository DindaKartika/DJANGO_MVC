from django.db import models as models
from django.db.models import CharField
from django.db.models import TextField


# Create your models here.
class Dokter(models.Model):
    nama = models.CharField(max_length = 255)
    telepon = models.CharField(max_length = 25)
    bidang = models.CharField(max_length=50)
    jadwal_praktek = models.DateTimeField()

class Pasien(models.Model):
    nama = models.CharField(max_length = 255)
    telepon = models.CharField(max_length = 25)
    alamat = models.CharField(max_length = 255)
    keluhan = models.TextField(max_length = 255)

class Resep(models.Model):
    nama = models.CharField(max_length = 255)
    total_harga = models.CharField(max_length = 25)
    kumpulan_obat = models.TextField(max_length = 255)

class Obat(models.Model):
    nama = models.CharField(max_length = 255)
    kandungan = models.TextField(max_length = 255)
    khasiat = models.TextField(max_length = 255)