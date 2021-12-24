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
class Merkezler(models.Model):
    merkez=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.merkez

class Vezifeler(models.Model):
    vezife_adi = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_vezife")
    merkez=models.ForeignKey(Merkezler, on_delete=models.CASCADE, related_name="merkez_vezife")
    def __str__(self):
        return self.vezife_adi
# class UserVezifeler(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
#     vezife = models.OneToOneField(Vezifeler, on_delete=models.CASCADE, related_name="vezife")
#     def __str__(self):
#         return f'{self.user}-{self.vezife}'

class Musteri(models.Model):
    asa = models.CharField(max_length=200)
    # soyad = models.CharField(max_length=50)
    # ata_adi = models.CharField(max_length=50)
    sv_image = models.ImageField(upload_to="media/")
    tel1 = models.CharField(max_length=50)
    tel2 = models.CharField(max_length=50)
    tel3 = models.CharField(max_length=50)
    tel4 = models.CharField(max_length=50)
    unvan = models.CharField(max_length=150)

class MusteriQeydler(models.Model):
    basliq=models.CharField(max_length=100)
    qeyd=models.TextField()
    musteri=models.ForeignKey(Musteri,on_delete=models.CASCADE, related_name="musteri_qeydler")

      

# class NagdQiymet(models.Model):
#     qiymet = models.FLoatField()
#     mehsul_qiymeti=models.OneToOneField(Mehsullar, on_delete=models.CASCADE, related_name="mehsul_qiymeti")
# class Kredit(models.Model):
#     qiymet = models.FLoatField()
#     ilkin_odenis = models.FLoatField(min=100.0)

