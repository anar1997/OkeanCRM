from django.db import models

from account.models import Merkezler, Musteri, User

# Create your models here.
class Kateqoriyalar(models.Model):
    kateqoriya=models.CharField(max_length=300)

    def __str__(self):
        return self.kateqoriya
class Anbar(models.Model):
    ad=models.CharField(max_length=100)
    merkez=models.ForeignKey(Merkezler, on_delete=models.CASCADE, related_name="merkez_anbar")
    
    def __str__(self) -> str:
        return self.ad

class AnbarQeydler(models.Model):
    basliq=models.CharField(max_length=100)
    qeyd=models.TextField()
    anbar=models.ForeignKey(Anbar, on_delete=models.CASCADE, related_name="anbar_qeyd")
    def __str__(self) -> str:
        return self.basliq
class Mehsullar(models.Model):
    mehsulun_adi=models.CharField(max_length=300)
    kateqoriya=models.ForeignKey(Kateqoriyalar, on_delete=models.CASCADE, related_name="mehsul_kateqoriya")
    anbar=models.ForeignKey(Anbar, on_delete=models.CASCADE, related_name="anbar_mehsul")
    qiymet=models.FloatField()
    def __str__(self) -> str:
        return self.mehsulun_adi
class Muqavile(models.Model):
    dealer=models.ForeignKey(User, on_delete=models.CASCADE, related_name="dealer")
    canvesser=models.ForeignKey(User, on_delete=models.CASCADE, related_name="canvesser")
    musteri=models.ForeignKey(Musteri, on_delete=models.CASCADE, related_name="musteri_muqavile")
    mehsul=models.ForeignKey(Mehsullar, on_delete=models.CASCADE, related_name="mehsul_muqavile")
    elektron_imza=models.ImageField(upload_to="media/")


    def __str__(self) -> str:
        return f"muqavile {self.musteri} - {self.mehsul}"

class Dates(models.Model):
    muqavile = models.ForeignKey(Muqavile, blank=True, null=True, related_name='muqavile_tarixi', on_delete=models.CASCADE)
    tarix = models.DateField(default=False, blank=True, null=True)
    qiymet = models.FloatField(null=True, blank=True)
    ilkin_odenis=models.FloatField()
    available = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.tarix} - {self.muqavile}"
