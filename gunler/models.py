from django.db import models
import account
import company
import pandas as pd
import datetime

# Create your models here.

class IstisnaIsci(models.Model):
    istisna_isciler = models.ManyToManyField('account.User', blank=True)
    tetil_gunleri = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        abstract = True


class IsciGunler(models.Model):
    isci = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name="is_gunleri")
    is_gunleri_count = models.PositiveBigIntegerField(default=0)
    qeyri_is_gunu_count = models.PositiveBigIntegerField(default=0)
    tetil_gunleri = models.CharField(max_length=500, null=True, blank=True)
    icaze_gunleri_odenisli = models.CharField(max_length=500, null=True, blank=True)
    icaze_gunleri_odenissiz = models.CharField(max_length=500, null=True, blank=True)
    tarix = models.DateField(editable=False)

    class Meta:
        ordering = ("pk",)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        indi = datetime.date.today()
        d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")

        next_m = d + pd.offsets.MonthBegin(1)
        if not self.id:
            self.tarix = next_m
        
        return super(IsciGunler, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.isci} - {self.is_gunleri_count} - {self.tarix}"

class HoldingGunler(models.Model):
    holding = models.ForeignKey('company.Holding', on_delete=models.CASCADE, related_name="is_gunleri")
    is_gunleri_count = models.PositiveBigIntegerField(default=0)
    qeyri_is_gunu_count = models.PositiveBigIntegerField(default=0)
    tetil_gunleri = models.CharField(max_length=500, null=True, blank=True)
    tarix = models.DateField(editable=False)
    
    class Meta:
        ordering = ("pk",)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        indi = datetime.date.today()
        d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")

        next_m = d + pd.offsets.MonthBegin(1)
        if not self.id:
            self.tarix = next_m
        
        return super(HoldingGunler, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.holding} - {self.is_gunleri_count} - {self.tarix}"


class ShirketGunler(models.Model):
    shirket = models.ForeignKey('company.Shirket', on_delete=models.CASCADE, related_name="is_gunleri")
    is_gunleri_count = models.PositiveBigIntegerField(default=0)
    qeyri_is_gunu_count = models.PositiveBigIntegerField(default=0)
    tetil_gunleri = models.CharField(max_length=500, null=True, blank=True)
    tarix = models.DateField(editable=False)

    class Meta:
        ordering = ("pk",)
        
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        indi = datetime.date.today()
        d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")

        next_m = d + pd.offsets.MonthBegin(1)
        if not self.id:
            self.tarix = next_m
        
        return super(ShirketGunler, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.shirket} - {self.is_gunleri_count} - {self.tarix}"

class OfisGunler(models.Model):
    ofis = models.ForeignKey('company.Ofis', on_delete=models.CASCADE, related_name="is_gunleri")
    is_gunleri_count = models.PositiveBigIntegerField(default=0)
    qeyri_is_gunu_count = models.PositiveBigIntegerField(default=0)
    tetil_gunleri = models.CharField(max_length=500, null=True, blank=True)
    tarix = models.DateField(editable=False)

    class Meta:
        ordering = ("pk",)
        
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        indi = datetime.date.today()
        d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")

        next_m = d + pd.offsets.MonthBegin(1)
        if not self.id:
            self.tarix = next_m
        
        return super(OfisGunler, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.ofis} - {self.is_gunleri_count} - {self.tarix}"

class KomandaGunler(models.Model):
    komanda = models.ForeignKey('company.Komanda', on_delete=models.CASCADE, related_name="is_gunleri")
    is_gunleri_count = models.PositiveBigIntegerField(default=0)
    qeyri_is_gunu_count = models.PositiveBigIntegerField(default=0)
    tetil_gunleri = models.CharField(max_length=500, null=True, blank=True)
    tarix = models.DateField(editable=False)

    class Meta:
        ordering = ("pk",)
        
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        indi = datetime.date.today()
        d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")

        next_m = d + pd.offsets.MonthBegin(1)
        if not self.id:
            self.tarix = next_m
        
        return super(KomandaGunler, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.komanda} - {self.is_gunleri_count} - {self.tarix}"

class VezifeGunler(models.Model):
    vezife = models.ForeignKey('company.Vezifeler', on_delete=models.CASCADE, related_name="is_gunleri")
    is_gunleri_count = models.PositiveBigIntegerField(default=0)
    qeyri_is_gunu_count = models.PositiveBigIntegerField(default=0)
    tetil_gunleri = models.CharField(max_length=500, null=True, blank=True)
    tarix = models.DateField(editable=False)

    class Meta:
        ordering = ("pk",)
        
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        indi = datetime.date.today()
        d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")

        next_m = d + pd.offsets.MonthBegin(1)
        if not self.id:
            self.tarix = next_m
        
        return super(VezifeGunler, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.vezife} - {self.is_gunleri_count} - {self.tarix}"

class ShobeGunler(models.Model):
    shobe = models.ForeignKey('company.Shobe', on_delete=models.CASCADE, related_name="is_gunleri")
    is_gunleri_count = models.PositiveBigIntegerField(default=0)
    qeyri_is_gunu_count = models.PositiveBigIntegerField(default=0)
    tetil_gunleri = models.CharField(max_length=500, null=True, blank=True)
    tarix = models.DateField(editable=False)

    class Meta:
        ordering = ("pk",)
        
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        indi = datetime.date.today()
        d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")

        next_m = d + pd.offsets.MonthBegin(1)
        if not self.id:
            self.tarix = next_m
        
        return super(ShobeGunler, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.shobe} - {self.is_gunleri_count} - {self.tarix}"


# ----------------------------------------------------------------------------------

class HoldingIstisnaIsci(IstisnaIsci):
    holding_gunler = models.ForeignKey(HoldingGunler, on_delete=models.CASCADE, related_name="istisna_isci")

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.holding_gunler} - {self.istisna_isciler} - {self.tetil_gunleri}"

class ShirketIstisnaIsci(IstisnaIsci):
    shirket_gunler = models.ForeignKey(ShirketGunler, on_delete=models.CASCADE, related_name="istisna_isci")

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.shirket_gunler} - {self.istisna_isciler} - {self.tetil_gunleri}"

class OfisIstisnaIsci(IstisnaIsci):
    ofis_gunler = models.ForeignKey(OfisGunler, on_delete=models.CASCADE, related_name="istisna_isci")

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.ofis_gunler} - {self.istisna_isciler} - {self.tetil_gunleri}"

class ShobeIstisnaIsci(IstisnaIsci):
    shobe_gunler = models.ForeignKey(ShobeGunler, on_delete=models.CASCADE, related_name="istisna_isci")

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.shobe_gunler} - {self.istisna_isciler} - {self.tetil_gunleri}"

class KomandaIstisnaIsci(IstisnaIsci):
    komanda_gunler = models.ForeignKey(KomandaGunler, on_delete=models.CASCADE, related_name="istisna_isci")

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.komanda_gunler} - {self.istisna_isciler} - {self.tetil_gunleri}"

class VezifeIstisnaIsci(IstisnaIsci):
    vezife_gunler = models.ForeignKey(VezifeGunler, on_delete=models.CASCADE, related_name="istisna_isci")

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.vezife_gunler} - {self.istisna_isciler} - {self.tetil_gunleri}"