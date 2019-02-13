from django.db import models

# Create your models here.
from django.db import models
from django.db.models import CharField
from django.db.models import TextField

# Create your models here.
class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length = 255)
    telepon = models.CharField(max_length = 25)
    jabatan = models.CharField(max_length = 50)

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length = 255)
    telepon = models.CharField(max_length = 25)
    absen = models.CharField(max_length = 3)
    nilai_rata2 = models.CharField(max_length = 3)

class MataPelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length = 100)
    jadwal_dimulai = models.DateTimeField()
    jadwal_berakhir = models.DateTimeField()

    def __str__(self):
        return self.nama_pelajaran

class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length = 255)
    telepon = models.CharField(max_length = 25)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE, default = "")

class Challenge(models.Model):
    nama_challenge = models.CharField(max_length = 255)
    banyak_soal = models.CharField(max_length = 3)
    bobot_nilai = models.CharField(max_length = 4)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete = models.CASCADE, default = "")

class LiveCode(models.Model):
    nama_live_code = models.CharField(max_length = 255)
    banyak_soal = models.CharField(max_length = 3)
    bobot_nilai = models.CharField(max_length = 4)
    tanggal_pelaksanaan = models.DateTimeField()
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete = models.CASCADE, default = "")