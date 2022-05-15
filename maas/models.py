import django
from django.db import models
import datetime

class AbstractPrim(models.Model):
    KREDIT = 'KREDİT'
    NAGD = 'NƏĞD'
    ODENIS_USLUBU_CHOICES = [
        (KREDIT, "KREDİT"),
        (NAGD, "NƏĞD"),
    ]

    prim_status = models.ForeignKey('account.IsciStatus', on_delete=models.SET_NULL, null=True)
    mehsul = models.ForeignKey('mehsullar.Mehsullar', on_delete=models.CASCADE, null=True)
    satis_meblegi = models.FloatField(default=0)
    odenis_uslubu =  models.CharField(
        max_length=20,
        choices=ODENIS_USLUBU_CHOICES,
        default=NAGD
    )
    vezife = models.ForeignKey('company.Vezifeler', on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True

class VanLeaderPrim(AbstractPrim):
    komandaya_gore_prim = models.FloatField(default=0, blank=True)
    fix_maas = models.FloatField(default=0, blank=True)

    def __str__(self) -> str:
        return f"{self.prim_status} - {self.komandaya_gore_prim}"

class DealerPrim(AbstractPrim):
    komandaya_gore_prim = models.FloatField(default=0, blank=True)
    fix_maas = models.FloatField(default=0, blank=True)

    def __str__(self) -> str:
        return f"{self.prim_status} - {self.komandaya_gore_prim}"

class OfficeLeaderPrim(AbstractPrim):
    odenis_uslubu = None
    ofise_gore_prim = models.FloatField(default=0, blank=True)
    fix_maas = models.FloatField(default=0, blank=True)

    def __str__(self) -> str:
        return f"{self.prim_status} - {self.ofise_gore_prim}"

class CanvasserPrim(AbstractPrim):
    odenis_uslubu = None
    satis0 = models.FloatField(default=0, blank=True)
    satis1_8 = models.FloatField(default=0, blank=True)
    satis9_14 = models.FloatField(default=0, blank=True)
    satis15p = models.FloatField(default=0, blank=True)
    satis20p = models.FloatField(default=0, blank=True)
    komandaya_gore_prim = models.FloatField(default=0, blank=True)
    ofise_gore_prim = models.FloatField(default=0, blank=True)
    fix_maas = models.FloatField(default=0, blank=True)

    def __str__(self) -> str:
        return f"{self.prim_status} - {self.ofise_gore_prim}"

# -----------------------------------------------------------------------------------------------------------------------------

class Avans(models.Model):
    isci = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name="isci_avans")
    mebleg = models.FloatField(default=0, blank=True)
    yarim_ay_emek_haqqi = models.PositiveBigIntegerField(default=0, blank=True)
    qeyd = models.TextField()
    avans_tarixi = models.DateField(default=django.utils.timezone.now, null=True, blank=True)
    
    class Meta:
        ordering = ("avans_tarixi",)

    def __str__(self) -> str:
        return f"{self.isci} {self.avans_tarixi}"

class Kesinti(models.Model):
    isci = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name="isci_kesinti")
    mebleg = models.FloatField(default=0, blank=True)
    qeyd = models.TextField()
    kesinti_tarixi = models.DateField(default=django.utils.timezone.now, null=True, blank=True)
    
    class Meta:
        ordering = ("kesinti_tarixi",)

    def __str__(self) -> str:
        return f"{self.isci} {self.kesinti_tarixi}"

class Bonus(models.Model):
    isci = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name="isci_bonus")
    mebleg = models.FloatField(default=0, blank=True)
    qeyd = models.TextField()
    bonus_tarixi = models.DateField(default=django.utils.timezone.now, null=True, blank=True)
    
    class Meta:
        ordering = ("bonus_tarixi",)

    def __str__(self) -> str:
        return f"{self.isci} {self.mebleg} {self.bonus_tarixi}"
 
class MaasGoruntuleme(models.Model):
    isci = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name="isci_maas_goruntuleme")
    satis_sayi = models.PositiveBigIntegerField(default=0, blank=True)
    satis_meblegi = models.FloatField(default=0, blank=True)
    yekun_maas = models.FloatField(default=0, blank=True)
    tarix = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.isci} {self.yekun_maas} {self.tarix}"