from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from mehsullar.models import Stok

from .managers import CustomUserManager

class Holding(models.Model):
    holding_adi=models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return self.holding_adi

class Shirket(models.Model):
    shirket_adi=models.CharField(max_length=200, unique=True)
    holding = models.ForeignKey(Holding, on_delete=models.DO_NOTHING, related_name="holding_shirket")

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return self.shirket_adi

class Ofis(models.Model):
    ofis_adi=models.CharField(max_length=100)
    shirket=models.ForeignKey(Shirket, on_delete=models.CASCADE, related_name="shirket_ofis")

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.ofis_adi} - {self.shirket}"


class Shobe(models.Model):
    shobe_adi=models.CharField(max_length=200)
    ofis=models.ForeignKey(Ofis, on_delete=models.CASCADE, null=True, related_name="shobe")

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.shobe_adi} - {self.ofis}"

class Vezifeler(models.Model):
    vezife_adi = models.CharField(max_length=50)
    shobe=models.ForeignKey(Shobe, on_delete=models.CASCADE, null=True, related_name="shobe_vezife")
    shirket=models.ForeignKey(Shirket, on_delete=models.CASCADE, related_name="shirket_vezifeleri")

    class Meta:
        ordering = ("pk",)

    def __str__(self):
        return f"{self.vezife_adi}-{self.shobe}"

class Komanda(models.Model):
    komanda_adi = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self):
        return self.komanda_adi

class Bonus(models.Model):
    KREDIT = 'KREDIT'
    NAGD = 'NAGD'
    ODENIS_USLUBU_CHOICES = [
        (KREDIT, "KREDIT"),
        (NAGD, "NAGD"),
    ]

    status = models.CharField(max_length=250, null=True)
    stok = models.ForeignKey(Stok, on_delete=models.CASCADE, null=True, related_name="stok_bonus")
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
    username = None
    first_name = None
    last_name = None

    email = models.EmailField(_('email address'), unique=True)
    asa= models.CharField(max_length=200)
    dogum_tarixi= models.DateField(null=True, blank=True)
    ishe_baslama_tarixi= models.DateField(auto_now_add = True, null=True, blank=True)
    last_login = models.DateTimeField(auto_now = True, null=True, blank=True)
    tel1=models.CharField(max_length=200)
    tel2=models.CharField(max_length=200)
    sv_image=models.ImageField(upload_to="media/")
    shirket=models.ForeignKey(Shirket, on_delete=models.SET_NULL, null=True, related_name="ishci")
    ofis=models.ForeignKey(Ofis, on_delete=models.SET_NULL, null=True, related_name="ishci")
    shobe=models.ForeignKey(Shobe, on_delete=models.SET_NULL, null=True, related_name="ishci")
    vezife = models.ForeignKey(Vezifeler, on_delete=models.SET_NULL, related_name="user_vezife", null=True, blank=True)
    komanda = models.OneToOneField(Komanda, on_delete=models.SET_NULL, related_name="user_komanda", null=True, blank=True)
    status = models.ForeignKey(Bonus, on_delete=models.SET_NULL, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ("pk",)

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

    class Meta:
        ordering = ("pk",)

    def __str__(self):
        return self.asa

class MusteriQeydler(models.Model):
    basliq=models.CharField(max_length=100)
    qeyd=models.TextField()
    musteri=models.ForeignKey(Musteri,on_delete=models.CASCADE, related_name="musteri_qeydler")

    class Meta:
        ordering = ("pk",)

    def __str__(self):
        return self.basliq

# Kassa Ve Transferler **************************

class OfisKassa(models.Model):
    ofis = models.ForeignKey(Ofis, on_delete=models.CASCADE, related_name="ofis_kassa")
    balans = models.FloatField()

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.ofis} -> {self.balans}"

class ShirketKassa(models.Model):
    shirket = models.ForeignKey(Shirket, on_delete=models.CASCADE, related_name="shirket_kassa")
    balans = models.FloatField()

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.shirket} -> {self.balans}"


class HoldingKassa(models.Model):
    holding = models.ForeignKey(Holding, on_delete=models.CASCADE, related_name="holding_kassa")
    balans = models.FloatField()

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.holding} -> {self.balans}"

class OfisdenShirketeTransfer(models.Model):
    ofis_kassa = models.ForeignKey(OfisKassa, on_delete=models.CASCADE, null=True, related_name="ofisden_shirkete_transfer")
    shirket_kassa = models.ForeignKey(ShirketKassa, on_delete=models.CASCADE, null=True, related_name="ofisden_shirkete_transfer")
    transfer_meblegi = models.FloatField()
    transfer_tarixi = models.DateField(auto_now = True)
    transfer_qeydi = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.ofis} -> {self.shirket} {self.transfer_meblegi} azn"

class ShirketdenOfislereTransfer(models.Model):
    shirket_kassa = models.ForeignKey(ShirketKassa, on_delete=models.CASCADE, null=True, related_name="shirketden_ofise_transfer")
    ofis_kassa = models.ManyToManyField(OfisKassa, related_name="shirketden_ofise_transfer")
    transfer_meblegi = models.FloatField()
    transfer_tarixi = models.DateField(auto_now = True)
    transfer_qeydi = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.shirket} -> {self.ofis} {self.transfer_meblegi} azn"

class ShirketdenHoldingeTransfer(models.Model):
    shirket_kassa = models.ForeignKey(ShirketKassa, on_delete=models.CASCADE, null=True, related_name="shirketden_holdinge_transfer")
    holding_kassa = models.ForeignKey(HoldingKassa, on_delete=models.CASCADE, null=True, related_name="shirketden_holdinge_transfer")
    transfer_meblegi = models.FloatField()
    transfer_tarixi = models.DateField(auto_now = True)
    transfer_qeydi = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.shirket} -> {self.holding} {self.transfer_meblegi} azn"

class HoldingdenShirketlereTransfer(models.Model):
    holding_kassa = models.ForeignKey(HoldingKassa, on_delete=models.CASCADE, null=True, related_name="holdingden_shirkete_transfer")
    shirket_kassa = models.ManyToManyField(ShirketKassa, related_name="holdingden_shirkete_transfer")
    transfer_meblegi = models.FloatField()
    transfer_tarixi = models.DateField(auto_now = True)
    transfer_qeydi = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.shirket} -> {self.holding} {self.transfer_meblegi} azn"


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


