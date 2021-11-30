from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Vezifeler(models.Model):
    vezife_adi = models.CharField(max_length=50)
    def __str__(self):
        return self.vezife_adi

class UserVezifeler(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    vezife = models.OneToOneField(Vezifeler, on_delete=models.CASCADE, related_name="vezife")
    def __str__(self):
        return f'{self.user}-{self.vezife}'

class Musteri(models.Model):
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=50)
    ata_adi = models.CharField(max_length=50)
    sv_image = models.ImageFIeld(upload_to="media/")
    tel1 = models.CharField(max_length=50)
    tel2 = models.CharField(max_length=50)
    tel3 = models.CharField(max_length=50)
    tel4 = models.CharField(max_length=50)
    unvan = models.CharField(max_length=150)

class Mehsullar(models.Model):
    mehsulun_adi=models.CharField(max_length=300)

class Kateqoriyalar(models.Model):
    kateqoriya=models.CharField(max_length=300)

class MehsulKateqoriya(models.Model):
    mehsul=models.OneToOneField(Mehsullar, on_delete=models.CASCADE, related_name="mehsul")
    kateqoriya=models.OneToOneField(Kateqoriyalar, on_delete=models.CASCADE, related_name="kateqoriya")

class NagdQiymet(models.Model):
    qiymet = models.FLoatField()
    mehsul_qiymeti=models.OneToOneField(Mehsullar, on_delete=models.CASCADE, related_name="mehsul_qiymeti")
class Kredit(models.Model):
    qiymet = models.FLoatField()
    ilkin_odenis = models.FLoatField(min=100.0)
    