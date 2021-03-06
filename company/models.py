from django.db import models

# Create your models here.
class Holding(models.Model):
    holding_adi = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return self.holding_adi


class Shirket(models.Model):
    shirket_adi = models.CharField(max_length=200, unique=True)
    holding = models.ForeignKey(Holding, on_delete=models.DO_NOTHING, related_name="holding_shirket")

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return self.shirket_adi


class Ofis(models.Model):
    ofis_adi = models.CharField(max_length=100)
    shirket = models.ForeignKey(Shirket, on_delete=models.CASCADE, related_name="shirket_ofis")

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.ofis_adi} - {self.shirket}"


class Shobe(models.Model):
    shobe_adi = models.CharField(max_length=200)
    ofis = models.ForeignKey(Ofis, on_delete=models.CASCADE, null=True, related_name="shobe")

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.shobe_adi} - {self.ofis}"


class Vezifeler(models.Model):
    vezife_adi = models.CharField(max_length=50)
    shobe = models.ForeignKey(Shobe, on_delete=models.CASCADE, null=True, related_name="shobe_vezife")
    shirket = models.ForeignKey(Shirket, on_delete=models.CASCADE, related_name="shirket_vezifeleri")

    class Meta:
        ordering = ("pk",)

    def __str__(self):
        return f"{self.vezife_adi}-{self.shobe}"


class Komanda(models.Model):
    komanda_adi = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ("pk",)

    def __str__(self):
        return self.komanda_adi


# Kassa Ve Transferler **************************

class OfisKassa(models.Model):
    ofis = models.ForeignKey(Ofis, on_delete=models.CASCADE, related_name="ofis_kassa")
    balans = models.FloatField(default=0)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.ofis} -> {self.balans}"


class ShirketKassa(models.Model):
    shirket = models.ForeignKey(Shirket, on_delete=models.CASCADE, related_name="shirket_kassa")
    balans = models.FloatField(default=0)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.shirket} -> {self.balans}"


class HoldingKassa(models.Model):
    holding = models.ForeignKey(Holding, on_delete=models.CASCADE, related_name="holding_kassa")
    balans = models.FloatField(default=0)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.holding} -> {self.balans}"


class OfisdenShirketeTransfer(models.Model):
    transfer_eden = models.ForeignKey('account.User', on_delete=models.CASCADE, null=True,
                                      related_name="user_ofis_shirket_transfer")
    ofis_kassa = models.ForeignKey(OfisKassa, on_delete=models.CASCADE, null=True,
                                   related_name="ofisden_shirkete_transfer")
    shirket_kassa = models.ForeignKey(ShirketKassa, on_delete=models.CASCADE, null=True,
                                      related_name="ofisden_shirkete_transfer")
    transfer_meblegi = models.FloatField(default=0)
    transfer_tarixi = models.DateField(auto_now=True)
    transfer_qeydi = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.ofis_kassa} -> {self.shirket_kassa} {self.transfer_meblegi} azn"


class ShirketdenOfislereTransfer(models.Model):
    transfer_eden = models.ForeignKey('account.User', on_delete=models.CASCADE, null=True,
                                      related_name="user_shirket_ofis_transfer")
    shirket_kassa = models.ForeignKey(ShirketKassa, on_delete=models.CASCADE, null=True,
                                      related_name="shirketden_ofise_transfer")
    ofis_kassa = models.ManyToManyField(OfisKassa, related_name="shirketden_ofise_transfer")
    transfer_meblegi = models.FloatField(default=0)
    transfer_tarixi = models.DateField(auto_now=True)
    transfer_qeydi = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.shirket_kassa} -> {self.ofis_kassa} {self.transfer_meblegi} azn"


class ShirketdenHoldingeTransfer(models.Model):
    transfer_eden = models.ForeignKey('account.User', on_delete=models.CASCADE, null=True,
                                      related_name="user_shirket_holding_transfer")
    shirket_kassa = models.ForeignKey(ShirketKassa, on_delete=models.CASCADE, null=True,
                                      related_name="shirketden_holdinge_transfer")
    holding_kassa = models.ForeignKey(HoldingKassa, on_delete=models.CASCADE, null=True,
                                      related_name="shirketden_holdinge_transfer")
    transfer_meblegi = models.FloatField(default=0)
    transfer_tarixi = models.DateField(auto_now=True)
    transfer_qeydi = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.shirket_kassa} -> {self.holding_kassa} {self.transfer_meblegi} azn"


class HoldingdenShirketlereTransfer(models.Model):
    transfer_eden = models.ForeignKey('account.User', on_delete=models.CASCADE, null=True,
                                      related_name="user_holding_shirket_transfer")
    holding_kassa = models.ForeignKey(HoldingKassa, on_delete=models.CASCADE, null=True,
                                      related_name="holdingden_shirkete_transfer")
    shirket_kassa = models.ManyToManyField(ShirketKassa, related_name="holdingden_shirkete_transfer")
    transfer_meblegi = models.FloatField(default=0)
    transfer_tarixi = models.DateField(auto_now=True)
    transfer_qeydi = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.holding_kassa} -> {self.shirket_kassa} {self.transfer_meblegi} azn"


# Medaxil Ve Mexaric **************************
class HoldingKassaMedaxil(models.Model):
    medaxil_eden = models.ForeignKey('account.User', on_delete=models.SET_NULL, null=True,
                                     related_name="user_holding_medaxil")
    holding_kassa = models.ForeignKey(HoldingKassa, on_delete=models.CASCADE, null=True,
                                      related_name="holding_kassa_medaxil")
    mebleg = models.FloatField(default=0)
    qeyd = models.TextField(null=True, blank=True)
    medaxil_tarixi = models.DateField(default=None)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.holding_kassa} kassas??na {self.mebleg} azn m??daxil edildi"


class HoldingKassaMexaric(models.Model):
    mexaric_eden = models.ForeignKey('account.User', on_delete=models.SET_NULL, null=True,
                                     related_name="user_holding_mexaric")
    holding_kassa = models.ForeignKey(HoldingKassa, on_delete=models.CASCADE, null=True,
                                      related_name="holding_kassa_mexaric")
    mebleg = models.FloatField(default=0)
    qebzin_resmi = models.FileField(upload_to="media/%Y/%m/%d/", null=True, blank=True)
    qeyd = models.TextField(null=True, blank=True)
    mexaric_tarixi = models.DateField(default=None)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.holding_kassa} kassas??ndan {self.mebleg} azn m??xaric edildi"


# -----------------------------------------------------

class ShirketKassaMedaxil(models.Model):
    medaxil_eden = models.ForeignKey('account.User', on_delete=models.SET_NULL, null=True,
                                     related_name="user_shirket_medaxil")
    shirket_kassa = models.ForeignKey(ShirketKassa, on_delete=models.CASCADE, null=True,
                                      related_name="shirket_kassa_medaxil")
    mebleg = models.FloatField(default=0)
    qeyd = models.TextField(null=True, blank=True)
    medaxil_tarixi = models.DateField(default=None)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.shirket_kassa} kassas??na {self.mebleg} azn m??daxil edildi"


class ShirketKassaMexaric(models.Model):
    mexaric_eden = models.ForeignKey('account.User', on_delete=models.SET_NULL, null=True,
                                     related_name="user_shirket_mexaric")
    shirket_kassa = models.ForeignKey(ShirketKassa, on_delete=models.CASCADE, null=True,
                                      related_name="shirket_kassa_mexaric")
    mebleg = models.FloatField(default=0)
    qebzin_resmi = models.FileField(upload_to="media/%Y/%m/%d/", null=True, blank=True)
    qeyd = models.TextField(null=True, blank=True)
    mexaric_tarixi = models.DateField(default=None)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.shirket_kassa} kassas??ndan {self.mebleg} azn m??xaric edildi"


# -----------------------------------------------------

class OfisKassaMedaxil(models.Model):
    medaxil_eden = models.ForeignKey('account.User', on_delete=models.SET_NULL, null=True,
                                     related_name="user_ofis_medaxil")
    ofis_kassa = models.ForeignKey(OfisKassa, on_delete=models.CASCADE, null=True, related_name="ofis_kassa_medaxil")
    mebleg = models.FloatField(default=0)
    qeyd = models.TextField(null=True, blank=True)
    medaxil_tarixi = models.DateField(default=None)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.ofis_kassa} kassas??na {self.mebleg} azn m??daxil edildi"


class OfisKassaMexaric(models.Model):
    mexaric_eden = models.ForeignKey('account.User', on_delete=models.SET_NULL, null=True,
                                     related_name="user_ofis_mexaric")
    ofis_kassa = models.ForeignKey(OfisKassa, on_delete=models.CASCADE, null=True, related_name="ofis_kassa_mexaric")
    mebleg = models.FloatField(default=0)
    qebzin_resmi = models.FileField(upload_to="media/%Y/%m/%d/", null=True, blank=True)
    qeyd = models.TextField(null=True, blank=True)
    mexaric_tarixi = models.DateField(default=None)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.ofis_kassa} kassas??ndan {self.mebleg} azn m??xaric edildi"

# -----------------------------------------------------

class MuqavileKreditor(models.Model):
    kreditor = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name="muqavile_kreditor")
    muqavile = models.ForeignKey('mehsullar.Muqavile', on_delete=models.CASCADE, related_name="kreditor")
    
    def __str__(self) -> str:
        return f"{self.kreditor.asa} {self.muqavile}"