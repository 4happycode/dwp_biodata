from django.db import models

# Create your models here.

class User(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.CharField(max_length=255)
    no_ktp = models.CharField(max_length=16)
    foto = models.ImageField(upload_to='media/photos/', blank=True, null=True)
    
    def __str__(self):
        return self.nama
    

class Pendidikan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pendidikan')
    sekolah = models.CharField(max_length=100)
    jurusan = models.CharField(max_length=100)
    tahun_masuk = models.IntegerField()
    tahun_lulus = models.IntegerField()

    def __str__(self):
        return f"{self.sekolah} - {self.jurusan}"


class PengalamanKerja(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pengalaman_kerja')
    perusahaan = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=100)
    tahun = models.IntegerField()
    keterangan = models.TextField()

    def __str__(self):
        return self.perusahaan
