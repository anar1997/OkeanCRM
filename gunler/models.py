from django.db import models

# Create your models here.

class Gunler(models.Model):
    gunler = models.CharField(max_length=500)


class IsciGunler(models.Model):
    is_gunleri = models.CharField(max_length=500)
    icazeli_gunleri = models.CharField(max_length=500)

