from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class IsciStatus(models.Model):
    status_adi = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.status_adi

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
    shirket=models.ForeignKey("company.Shirket", on_delete=models.SET_NULL, null=True, related_name="ishci")
    ofis=models.ForeignKey("company.Ofis", on_delete=models.SET_NULL, null=True, related_name="ishci")
    shobe=models.ForeignKey("company.Shobe", on_delete=models.SET_NULL, null=True, related_name="ishci")
    vezife = models.ForeignKey("company.Vezifeler", on_delete=models.SET_NULL, related_name="user_vezife", null=True, blank=True)
    komanda = models.OneToOneField("company.Komanda", on_delete=models.SET_NULL, related_name="user_komanda", null=True, blank=True)
    isci_status = models.ForeignKey(IsciStatus, on_delete=models.SET_NULL, null=True, blank=True)

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

class IsciSatisSayi(models.Model):
    tarix = models.DateField()
    isci = models.ForeignKey(User, on_delete=models.CASCADE, related_name="isci_satis_sayi")
    satis_sayi = models.PositiveIntegerField(default=0, null=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.isci} {self.tarix}-də {self.satis_sayi} satış etmişdir"