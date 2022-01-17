from django.db import models
from django.db.models.fields.related import ForeignKey

from account.models import Merkezler, Musteri, User, Shirket

# Create your models here.
# class Kateqoriyalar(models.Model):
#     kateqoriya=models.CharField(max_length=300)
#     shirket=models.ForeignKey(Shirket, on_delete=models.CASCADE, related_name="kateqoriya")

#     def __str__(self):
#         return self.kateqoriya
class Anbar(models.Model):
    ad=models.CharField(max_length=100)
    merkez=models.ForeignKey(Merkezler, on_delete=models.CASCADE, related_name="merkez_anbar")
    shirket=models.ForeignKey(Shirket, on_delete=models.CASCADE, related_name="anbar")
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
    # kateqoriya=models.ForeignKey(Kateqoriyalar, on_delete=models.CASCADE, related_name="mehsul_kateqoriya")
    anbar=models.ForeignKey(Anbar, on_delete=models.CASCADE, related_name="anbar_mehsul")
    qiymet=models.FloatField()
    shirket=models.ForeignKey(Shirket, on_delete=models.CASCADE, related_name="mehsul")
    say = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.mehsulun_adi


class Stock(models.Model):
    warehouse = models.ForeignKey(Anbar, null=True, on_delete=models.CASCADE)
    
    quantity = models.IntegerField(default=0)

    class Meta:
        unique_together = [["warehouse"]]
        ordering = ("pk",)

    def increase_stock(self, quantity: int, commit: bool = True):
        """Return given quantity of product to a stock."""
        self.quantity += quantity
        if commit:
            self.save(update_fields=["quantity"])

    def decrease_stock(self, quantity: int, commit: bool = True):
        self.quantity -= quantity
        if commit:
            self.save(update_fields=["quantity"])

class Emeliyyat(models.Model):
    mehsulun_sayi=models.IntegerField(default=0)
    gonderen=models.ForeignKey(Anbar, on_delete=models.CASCADE, related_name="gonderen")
    qebul_eden=models.ForeignKey(Anbar, on_delete=models.CASCADE, related_name="qebul_eden")
    gonderilen_mehsul=models.ForeignKey(Mehsullar, on_delete=models.CASCADE, related_name="gonderilen_mehsul")
    qeyd=models.TextField(default="")

    def __str__(self) -> str:
        return self.qeyd[:30]

class Hediyye(models.Model):
    hediyye_adi= models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.hediyye_adi
class Hediyye2(models.Model):
    hediyye_adi=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.hediyye_adi
class Hediyye3(models.Model):
    hediyye_adi=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.hediyye_adi
        
class Muqavile(models.Model):
    dealer=models.ForeignKey(User, on_delete=models.CASCADE, related_name="dealer")
    canvesser=models.ForeignKey(User, on_delete=models.CASCADE, related_name="canvesser")
    musteri=models.ForeignKey(Musteri, on_delete=models.CASCADE, related_name="musteri_muqavile")
    mehsul=models.ForeignKey(Mehsullar, on_delete=models.CASCADE, related_name="mehsul_muqavile")
    elektron_imza=models.ImageField(upload_to="media/")
    muqavile_tarixi=models.DateField(auto_now_add=True)
    shirket=models.ForeignKey(Shirket, on_delete=models.CASCADE, related_name="muqavile")
    status=models.BooleanField(default=False)
    hediyye=models.ForeignKey(Hediyye, on_delete=models.CASCADE, related_name="muqavile", null=True, blank=True)
    pdf=models.FileField(blank=True, null=True)
    def __str__(self) -> str:
        return f"muqavile {self.musteri} - {self.mehsul}"

class Dates(models.Model):
    muqavile = models.ForeignKey(Muqavile, blank=True, null=True, related_name='muqavilenin_tarixi', on_delete=models.CASCADE)
    tarix = models.DateField(default=False, blank=True, null=True)
    qiymet = models.FloatField(null=True, blank=True)
    ilkin_odenis=models.FloatField(blank=True, null=True)
    status = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.tarix} - {self.muqavile}"

