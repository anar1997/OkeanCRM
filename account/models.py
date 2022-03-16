from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

import mehsullar
from company.models import (
    Shirket,
    Ofis,
    Komanda,
    Shobe,
    Vezifeler
)

from .managers import CustomUserManager


class Bonus(models.Model):
    KREDIT = 'KREDIT'
    NAGD = 'NAGD'
    ODENIS_USLUBU_CHOICES = [
        (KREDIT, "KREDIT"),
        (NAGD, "NAGD"),
    ]

    status = models.CharField(max_length=250, null=True)
    stok = models.ForeignKey('mehsullar.Stok', on_delete=models.CASCADE, null=True, related_name="stok_bonus")
    satis_meblegi = models.FloatField(default=0)
    odenis_uslubu =  models.CharField(
        max_length=20,
        choices=ODENIS_USLUBU_CHOICES,
        default=NAGD
    )
    vezife = models.ForeignKey(Vezifeler, on_delete=models.SET_NULL, null=True, related_name="vezife_bonus")
    komandaya_gore_bonus = models.FloatField(default=0, null=True, blank=True)
    ofise_gore_bonus = models.FloatField(default=0, null=True, blank=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.status} - {self.komandaya_gore_bonus}"

class User(AbstractUser):
    first_name = None
    last_name = None

    asa= models.CharField(max_length=200)
    dogum_tarixi= models.DateField(null=True, blank=True)
    ishe_baslama_tarixi= models.DateField(auto_now_add = True, null=True, blank=True)
    last_login = models.DateTimeField(auto_now = True, null=True, blank=True)
    tel1=models.CharField(max_length=200)
    tel2=models.CharField(max_length=200)
    sv_image=models.ImageField(upload_to="media/%Y/%m/%d/", null=True, blank=True)
    shirket=models.ForeignKey(Shirket, on_delete=models.SET_NULL, null=True, related_name="ishci")
    ofis=models.ForeignKey(Ofis, on_delete=models.SET_NULL, null=True, related_name="ishci")
    shobe=models.ForeignKey(Shobe, on_delete=models.SET_NULL, null=True, related_name="ishci")
    vezife = models.ForeignKey(Vezifeler, on_delete=models.SET_NULL, related_name="user_vezife", null=True, blank=True)
    komanda = models.OneToOneField(Komanda, on_delete=models.SET_NULL, related_name="user_komanda", null=True, blank=True)
    status = models.ForeignKey(Bonus, on_delete=models.SET_NULL, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ("pk",)  

    def __str__(self):
        return self.username

class Bolge(models.Model):
    bolge_adi = models.CharField(max_length=300)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return self.bolge_adi


class Musteri(models.Model):
    asa = models.CharField(max_length=200)
    sv_image = models.ImageField(upload_to="media/%Y/%m/%d/", null=True, blank=True)
    tel1 = models.CharField(max_length=50)
    tel2 = models.CharField(max_length=50, null=True, blank=True)
    tel3 = models.CharField(max_length=50, null=True, blank=True)
    tel4 = models.CharField(max_length=50, null=True, blank=True)
    unvan = models.TextField()
    bolge = models.ForeignKey(Bolge, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self):
        return self.asa

class MusteriQeydler(models.Model):
    qeyd=models.TextField()
    musteri=models.ForeignKey(Musteri,on_delete=models.CASCADE, related_name="musteri_qeydler")

    class Meta:
        ordering = ("pk",)

    def __str__(self):
        return f"{self.musteri} -- {self.qeyd[:20]}"

#  Maas ve Bonus **************************

class Maas(models.Model):
    FIX = 'FIX'
    BONUS = 'BONUS'
    BONUS_FIX = 'BONUS-FIX'
    MAAS_USLUBU_CHOICES = [
        (FIX, "FIX"), 
        (BONUS, "BONUS"),
        (BONUS_FIX, 'BONUS-FIX')
    ]

    maas_uslubu = models.CharField(
        max_length=20,
        choices=MAAS_USLUBU_CHOICES,
        default=FIX
    )

    isci = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="isci_maas")
    verilecek_maas = models.FloatField(null=True, blank=True)
    maas_tarixi = models.DateField(null=True, blank=True)

    odenme_status = models.BooleanField(default=False)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return self.maas_uslubu
 

class IsciSatisSayi(models.Model):
    tarix = models.DateField()
    isci = models.ForeignKey(User, on_delete=models.CASCADE, related_name="isci_satis_sayi")
    satis_sayi = models.PositiveIntegerField(default=0, null=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.isci} {self.tarix}-də {self.satis_sayi} satış etmişdir"