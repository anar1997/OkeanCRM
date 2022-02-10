from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class Shirket(models.Model):
    shirket_adi=models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.shirket_adi

class Ofis(models.Model):
    ofis_adi=models.CharField(max_length=100)
    shirket=models.ForeignKey(Shirket, on_delete=models.CASCADE, related_name="shirket_ofis")
    def __str__(self) -> str:
        return f"{self.ofis_adi} - {self.shirket}"


class Shobe(models.Model):
    shobe_adi=models.CharField(max_length=200)
    ofis=models.ForeignKey(Ofis, on_delete=models.CASCADE, null=True, related_name="shobe")
    def __str__(self) -> str:
        return f"{self.shobe_adi} - {self.ofis}"

class Vezifeler(models.Model):
    vezife_adi = models.CharField(max_length=50)
    shobe=models.ForeignKey(Shobe, on_delete=models.CASCADE, null=True, related_name="shobe_vezife")
    shirket=models.ForeignKey(Shirket, on_delete=models.CASCADE, related_name="shirket_vezifeleri")
    def __str__(self):
        return f"{self.vezife_adi}-{self.shobe}"

class Komanda(models.Model):
    komanda_adi = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.komanda_adi

class User(AbstractUser):
    username = None
    first_name = None
    last_name = None

    email = models.EmailField(_('email address'), unique=True)
    asa= models.CharField(max_length=200)
    maas= models.FloatField(default=0)
    dogum_tarixi= models.DateField(null=True, blank=True)
    ishe_baslama_tarixi= models.DateField(auto_now_add = True, null=True, blank=True)
    last_login = models.DateTimeField(auto_now = True, null=True, blank=True)
    tel1=models.CharField(max_length=200)
    tel2=models.CharField(max_length=200)
    sv_image=models.ImageField(upload_to="media/")
    shirket=models.ForeignKey(Shirket, on_delete=models.CASCADE, null=True, related_name="ishci")
    ofis=models.ForeignKey(Ofis, on_delete=models.CASCADE, null=True, related_name="ishci")
    shobe=models.ForeignKey(Shobe, on_delete=models.CASCADE, null=True, related_name="ishci")
    vezife = models.ForeignKey(Vezifeler, on_delete=models.CASCADE, related_name="user_vezife", null=True, blank=True)
    komanda = models.OneToOneField(Komanda, on_delete=models.CASCADE, related_name="user_komanda", null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Musteri(models.Model):
    asa = models.CharField(max_length=200)
    sv_image = models.ImageField(upload_to="media/")
    tel1 = models.CharField(max_length=50)
    tel2 = models.CharField(max_length=50)
    tel3 = models.CharField(max_length=50)
    tel4 = models.CharField(max_length=50)
    unvan = models.TextField()

    def __str__(self):
        return self.asa

class MusteriQeydler(models.Model):
    basliq=models.CharField(max_length=100)
    qeyd=models.TextField()
    musteri=models.ForeignKey(Musteri,on_delete=models.CASCADE, related_name="musteri_qeydler")

    def __str__(self):
        return self.basliq

