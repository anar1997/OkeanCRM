from django.db import models
import account


class Anbar(models.Model):
    ad = models.CharField(max_length=100)
    ofis = models.ForeignKey('account.Ofis', on_delete=models.CASCADE, null=True, related_name="ofis_anbar")
    shirket = models.ForeignKey('account.Shirket', on_delete=models.CASCADE, null=True, related_name="shirket_anbar")

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.ad} - {self.ofis}"


class AnbarQeydler(models.Model):
    basliq = models.CharField(max_length=100)
    qeyd = models.TextField()
    anbar = models.ForeignKey(Anbar, on_delete=models.CASCADE, related_name="anbar_qeyd")

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return self.basliq


class Mehsullar(models.Model):
    mehsulun_adi = models.CharField(max_length=300)
    qiymet = models.FloatField()

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return self.mehsulun_adi


class Stok(models.Model):
    anbar = models.ForeignKey(Anbar, null=True, on_delete=models.CASCADE)
    mehsul = models.ForeignKey(Mehsullar, null=True, on_delete=models.CASCADE)
    say = models.IntegerField(default=0)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"stok -> {self.anbar}"


class Emeliyyat(models.Model):
    mehsulun_sayi = models.IntegerField(default=0)
    gonderen = models.ForeignKey(Anbar, on_delete=models.CASCADE, null=True, related_name="gonderen")
    qebul_eden = models.ForeignKey(Anbar, on_delete=models.CASCADE, null=True, related_name="qebul_eden")
    gonderilen_mehsul = models.ForeignKey(Mehsullar, on_delete=models.CASCADE, null=True, related_name="gonderilen_mehsul")
    qeyd = models.TextField(default="", null=True, blank=True)
    emeliyyat_tarixi = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"Əməliyyat ==> {self.gonderen} - {self.qebul_eden} {self.emeliyyat_tarixi}"


class Hediyye(models.Model):
    hediyye_adi = models.CharField(max_length=200)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return self.hediyye_adi


class Muqavile(models.Model):
    KREDIT = 'KREDIT'
    NAGD = 'NAGD'
    ODENIS_USLUBU_CHOICES = [
        (KREDIT, "KREDIT"),
        (NAGD, "NAGD"),
    ]

    vanleader = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name="vanleader", null=True, blank=True)
    dealer = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name="dealer", null=True, blank=True)
    canvesser = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name="canvesser", null=True, blank=True)
    musteri = models.ForeignKey('account.Musteri', on_delete=models.CASCADE, related_name="musteri_muqavile", null=True,
                                blank=True)
    mehsul = models.ForeignKey(Mehsullar, on_delete=models.CASCADE, related_name="mehsul_muqavile", null=True,
                               blank=True)
    elektron_imza = models.ImageField(upload_to="media/", null=True, blank=True)
    muqavile_tarixi = models.DateField(auto_now_add=True, null=True, blank=True)
    shirket = models.ForeignKey('account.Shirket', on_delete=models.CASCADE, related_name="muqavile", null=True, blank=True)
    ofis = models.ForeignKey('account.Ofis', on_delete=models.CASCADE, related_name="muqavile", null=True, blank=True)
    shobe = models.ForeignKey('account.Shobe', on_delete=models.CASCADE, related_name="muqavile", null=True, blank=True)
    status = models.BooleanField(default=False)
    dusen = models.BooleanField(default=False)
    hediyye1 = models.ForeignKey(Hediyye, on_delete=models.CASCADE, related_name="muqavile_hediyye1", null=True,
                                 blank=True)
    hediyye2 = models.ForeignKey(Hediyye, on_delete=models.CASCADE, related_name="muqavile_hediyye2", null=True,
                                 blank=True)
    hediyye3 = models.ForeignKey(Hediyye, on_delete=models.CASCADE, related_name="muqavile_hediyye3", null=True,
                                 blank=True)
    odenis_uslubu =  models.CharField(
        max_length=20,
        choices=ODENIS_USLUBU_CHOICES,
        default=NAGD
    )

    verilecek_ilkin_odenis = models.FloatField(blank=True, null=True)
    ilkin_odenis = models.FloatField(blank=True, null=True)
    ilkin_odenis_qaliq = models.FloatField(blank=True, null=True)
    ilkin_odenis_tarixi = models.DateField(blank=True, null=True)
    ilkin_odenis_qaliq_tarixi = models.DateField(blank=True, null=True)
    ilkin_odenis_status = models.BooleanField(default=False)

    pdf = models.FileField(blank=True, null=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"muqavile {self.musteri} - {self.mehsul}"

class OdemeTarix(models.Model):
    muqavile = models.ForeignKey(Muqavile, blank=True, null=True, related_name='odeme_tarixi',
                                 on_delete=models.CASCADE)
    tarix = models.DateField(default=False, blank=True, null=True)
    qiymet = models.FloatField(null=True, blank=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.tarix} - {self.muqavile}"


class Servis(models.Model):
    muqavile = models.ForeignKey(Muqavile, related_name="servis", null=True, on_delete=models.CASCADE)
    kartric1 = models.ForeignKey(Mehsullar, related_name="kartric1_servis", on_delete=models.CASCADE, null=True)
    kartric2 = models.ForeignKey(Mehsullar, related_name="kartric2_servis", on_delete=models.CASCADE, null=True)
    kartric3 = models.ForeignKey(Mehsullar, related_name="kartric3_servis", on_delete=models.CASCADE, null=True)
    kartric4 = models.ForeignKey(Mehsullar, related_name="kartric4_servis", on_delete=models.CASCADE, null=True)
    kartric5 = models.ForeignKey(Mehsullar, related_name="kartric5_servis", on_delete=models.CASCADE, null=True)
    kartric6 = models.ForeignKey(Mehsullar, related_name="kartric6_servis", on_delete=models.CASCADE, null=True)
    servis_tarix6ay = models.DateField(default=False, null=True, blank=True)
    servis_tarix18ay = models.DateField(default=False, null=True, blank=True)
    servis_tarix24ay = models.DateField(default=False, null=True, blank=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"servis-{self.muqavile}"