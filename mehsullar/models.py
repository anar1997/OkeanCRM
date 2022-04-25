import django
from django.db import models


class Anbar(models.Model):
    ad = models.CharField(max_length=100)
    ofis = models.ForeignKey('company.Ofis', on_delete=models.CASCADE, null=True, related_name="ofis_anbar")
    shirket = models.ForeignKey('company.Shirket', on_delete=models.CASCADE, null=True, related_name="shirket_anbar")

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.ad} - {self.ofis}"


class AnbarQeydler(models.Model):
    qeyd = models.TextField()
    anbar = models.ForeignKey(Anbar, on_delete=models.CASCADE, related_name="anbar_qeyd")

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.anbar} - {self.qeyd[:30]}"


class Mehsullar(models.Model):
    KARTRIC6AY = 'KARTRIC6AY'
    KARTRIC12AY = 'KARTRIC12AY'
    KARTRIC18AY = 'KARTRIC18AY'
    KARTRIC24AY = 'KARTRIC24AY'

    KARTRIC_NOVU_CHOICES = [
        (KARTRIC6AY, "KARTRIC6AY"),
        (KARTRIC12AY, "KARTRIC12AY"),
        (KARTRIC18AY, "KARTRIC18AY"),
        (KARTRIC24AY, "KARTRIC24AY"),
    ]
    
    mehsulun_adi = models.CharField(max_length=300)
    qiymet = models.FloatField()
    shirket = models.ForeignKey('company.Shirket', on_delete=models.CASCADE, null=True, related_name="shirket_mehsul")
    is_hediyye = models.BooleanField(default=False)

    kartric_novu =  models.CharField(
        max_length=50,
        choices=KARTRIC_NOVU_CHOICES,
        default=None,
        null=True,
        blank=True
    )


    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.shirket} şirkəti {self.mehsulun_adi} - {self.qiymet} AZN"


class Stok(models.Model):
    anbar = models.ForeignKey(Anbar, null=True, on_delete=models.CASCADE)
    mehsul = models.ForeignKey(Mehsullar, null=True, on_delete=models.CASCADE)
    say = models.IntegerField(default=0)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"stok -> {self.anbar} - {self.mehsul} - {self.say}"


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


class Muqavile(models.Model):
    KREDIT = 'KREDİT'
    NAGD = 'NƏĞD'
    IKI_DEFEYE_NEGD = "İKİ DƏFƏYƏ NƏĞD"

    ODENIS_USLUBU_CHOICES = [
        (NAGD, "NƏĞD"),
        (KREDIT, "KREDİT"),
        (IKI_DEFEYE_NEGD, "İKİ DƏFƏYƏ NƏĞD"),
    ]

    BITMIS = "BİTMİŞ"
    DAVAM_EDEN = "DAVAM EDƏN"
    DUSEN = "DÜŞƏN"
    YOXDUR = "YOXDUR"
    YENI_QRAFIK = "YENİ QRAFİK"

    YENI_QRAFIK_CHOICES = [
        (YENI_QRAFIK, "YENİ QRAFİK")
    ]

    MUQAVILE_STATUS_CHOICES = [
        (DAVAM_EDEN,"DAVAM EDƏN"),
        (BITMIS, "BİTMİŞ"),
        (DUSEN, "DÜŞƏN")
    ]

    ILKIN_ODENIS_STATUS_CHOICES = [
        (YOXDUR,"YOXDUR"),
        (BITMIS, "BİTMİŞ"),
        (DAVAM_EDEN,"DAVAM EDƏN"),   
    ]

    QALIQ_ILKIN_ODENIS_STATUS_CHOICES = [
        (YOXDUR,"YOXDUR"),
        (BITMIS, "BİTMİŞ"),
        (DAVAM_EDEN,"DAVAM EDƏN"),   
    ]

    NAGD_ODENIS_1_STATUS_CHOICES = [
        (YOXDUR,"YOXDUR"),
        (BITMIS, "BİTMİŞ"),
        (DAVAM_EDEN,"DAVAM EDƏN"),   
    ]

    NAGD_ODENIS_2_STATUS_CHOICES = [
        (YOXDUR,"YOXDUR"),
        (BITMIS, "BİTMİŞ"),
        (DAVAM_EDEN,"DAVAM EDƏN"),   
    ]

    DEYISMIS_MEHSUL = "DƏYİŞİLMİŞ MƏHSUL"

    DEYISMIS_MEHSUL_STATUS_CHOICES = [
        (DEYISMIS_MEHSUL, "DƏYİŞİLMİŞ MƏHSUL")
    ]

    vanleader = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name="vanleader", null=True, blank=True)
    dealer = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name="dealer", null=True, blank=True)
    canvesser = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name="canvesser", null=True, blank=True)
    musteri = models.ForeignKey('account.Musteri', on_delete=models.CASCADE, related_name="musteri_muqavile", null=True,
                                blank=True)
    mehsul = models.ForeignKey(Mehsullar, on_delete=models.CASCADE, related_name="mehsul_muqavile", null=True,
                               blank=True)
    mehsul_sayi = models.PositiveIntegerField(default=1, blank=True)
    muqavile_umumi_mebleg = models.FloatField(default=0, blank=True)
    elektron_imza = models.ImageField(upload_to="media/muqavile", null=True, blank=True)
    muqavile_tarixi = models.DateField(default=django.utils.timezone.now, blank=True)
    shirket = models.ForeignKey('company.Shirket', on_delete=models.CASCADE, related_name="muqavile", null=True, blank=True)
    ofis = models.ForeignKey('company.Ofis', on_delete=models.CASCADE, related_name="muqavile", null=True, blank=True)
    shobe = models.ForeignKey('company.Shobe', on_delete=models.CASCADE, related_name="muqavile", null=True, blank=True)
    
    odenis_uslubu =  models.CharField(
        max_length=20,
        choices=ODENIS_USLUBU_CHOICES,
        default=NAGD
    )

    negd_odenis_1 = models.FloatField(default=0, blank=True)
    negd_odenis_2 = models.FloatField(default=0, blank=True)
    
    negd_odenis_1_tarix = models.DateField(blank=True, null=True)
    negd_odenis_2_tarix = models.DateField(blank=True, null=True)

    yeni_qrafik_mebleg = models.FloatField(default=0, blank=True)
    yeni_qrafik_status = models.CharField(
        max_length=50,
        choices=YENI_QRAFIK_CHOICES,
        default=None,
        null=True,
        blank=True
    )

    deyisilmis_mehsul_status = models.CharField(
        max_length=50,
        choices=DEYISMIS_MEHSUL_STATUS_CHOICES,
        default=None,
        null=True,
        blank=True
    )


    negd_odenis_1_status = models.CharField(
        max_length=20,
        choices=NAGD_ODENIS_1_STATUS_CHOICES,
        default=YOXDUR
    )

    negd_odenis_2_status = models.CharField(
        max_length=20,
        choices=NAGD_ODENIS_2_STATUS_CHOICES,
        default=YOXDUR
    )

    muqavile_status = models.CharField(
        max_length=20,
        choices=MUQAVILE_STATUS_CHOICES,
        default=DAVAM_EDEN
    )

    kredit_muddeti = models.IntegerField(default=0, blank=True)
    ilkin_odenis = models.FloatField(blank=True, default=0)
    ilkin_odenis_qaliq = models.FloatField(blank=True, default=0)
    ilkin_odenis_tarixi = models.DateField(blank=True, null=True)
    ilkin_odenis_qaliq_tarixi = models.DateField(blank=True, null=True)

    ilkin_odenis_status = models.CharField(
        max_length=20,
        choices=ILKIN_ODENIS_STATUS_CHOICES,
        default=YOXDUR
    )

    qaliq_ilkin_odenis_status = models.CharField(
        max_length=20,
        choices=QALIQ_ILKIN_ODENIS_STATUS_CHOICES,
        default=YOXDUR
    )
    pdf = models.FileField(blank=True, null=True)

    kompensasiya_medaxil = models.FloatField(default=0, null=True, blank=True)
    kompensasiya_mexaric = models.FloatField(default=0, null=True, blank=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.pk}. muqavile {self.musteri} - {self.mehsul}"

class MuqavileHediyye(models.Model):
    mehsul = models.ForeignKey(Mehsullar, on_delete=models.SET_NULL, null=True, related_name="mehsul_hediyye")
    muqavile = models.ForeignKey(Muqavile, on_delete=models.CASCADE, related_name="muqavile_hediyye")

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"Hədiyyə --- {self.muqavile} - {self.mehsul}"

class OdemeTarix(models.Model):
    ODENEN = "ÖDƏNƏN"
    ODENMEYEN = "ÖDƏNMƏYƏN"
    
    BURAXILMIS_AY = "BURAXILMIŞ AY"
    NATAMAM_AY = "NATAMAM AY"
    RAZILASDIRILMIS_AZ_ODEME = "RAZILAŞDIRILMIŞ AZ ÖDƏMƏ"
    ARTIQ_ODEME = "ARTIQ ÖDƏMƏ"
    SON_AYIN_BOLUNMESI = "SON AYIN BÖLÜNMƏSİ"

    GECIKDIRME = "GECİKDİRMƏ"

    SIFIR_NOVBETI_AY = "SIFIR NÖVBƏTİ AY"
    SIFIR_SONUNCU_AY = "SIFIR SONUNCU AY"
    SIFIR_DIGER_AYLAR = "SIFIR DİGƏR AYLAR"

    NATAMAM_NOVBETI_AY = "NATAMAM NÖVBƏTİ AY"
    NATAMAM_SONUNCU_AY = "NATAMAM SONUNCU AY"
    NATAMAM_DIGER_AYLAR = "NATAMAM DİGƏR AYLAR"

    ARTIQ_BIR_AY = "ARTIQ_BİR_AY"
    ARTIQ_BUTUN_AYLAR = "ARTIQ_BÜTÜN_AYLAR"

    BORCU_BAGLA = "BORCU BAĞLA"

    ODEME_STATUS_CHOICES = [
        (ODENMEYEN,"ÖDƏNMƏYƏN"),
        (ODENEN, "ÖDƏNƏN"),
    ]

    SERTLI_ODEME_STATUSU = [
        (BURAXILMIS_AY, "BURAXILMIŞ AY"),
        (NATAMAM_AY, "NATAMAM AY"),
        (RAZILASDIRILMIS_AZ_ODEME, "RAZILAŞDIRILMIŞ AZ ÖDƏMƏ"),
        (ARTIQ_ODEME, "ARTIQ ÖDƏMƏ"),
        (SON_AYIN_BOLUNMESI, "SON AYIN BÖLÜNMƏSİ")
    ]

    GECIKDIRME_STATUS_CHOICES = [
        (GECIKDIRME, "GECİKDİRMƏ")
    ]

    SIFIR_STATUS_CHOICES = [
        (SIFIR_NOVBETI_AY,"SIFIR NÖVBƏTİ AY"),
        (SIFIR_SONUNCU_AY, "SIFIR SONUNCU AY"),
        (SIFIR_DIGER_AYLAR, "SIFIR DİGƏR AYLAR")
    ]

    NATAMAM_STATUS_CHOICES = [
        (NATAMAM_NOVBETI_AY,"NATAMAM NÖVBƏTİ AY"),
        (NATAMAM_SONUNCU_AY, "NATAMAM SONUNCU AY"),
        (NATAMAM_DIGER_AYLAR, "NATAMAM DİGƏR AYLAR")
    ]

    ARTIQ_ODEME_STATUS_CHOICES = [
        (ARTIQ_BIR_AY,"ARTIQ_BİR_AY"),
        (ARTIQ_BUTUN_AYLAR, "ARTIQ_BÜTÜN_AYLAR")
    ]

    BORCU_BAGLA_STATUS_CHOICES = [
        (BORCU_BAGLA,"BORCU BAĞLA")
    ]

    muqavile = models.ForeignKey(Muqavile, blank=True, null=True, related_name='odeme_tarixi',
                                 on_delete=models.CASCADE)
    tarix = models.DateField(default=False, blank=True, null=True)
    qiymet = models.FloatField(default=0, blank=True)
    odenme_status = models.CharField(
        max_length=30,
        choices=ODEME_STATUS_CHOICES,
        default=ODENMEYEN
    )

    sertli_odeme_status = models.CharField(
        max_length=50,
        choices=SERTLI_ODEME_STATUSU,
        default=None,
        null=True,
        blank=True
    )

    borcu_bagla_status = models.CharField(
        max_length=30,
        choices=BORCU_BAGLA_STATUS_CHOICES,
        default=None,
        null=True,
        blank=True
    )

    gecikdirme_status = models.CharField(
        max_length=30,
        choices=GECIKDIRME_STATUS_CHOICES,
        default=None,
        null=True,
        blank=True
    )

    buraxilmis_ay_alt_status = models.CharField(
        max_length=20,
        choices=SIFIR_STATUS_CHOICES,
        default=None,
        null=True,
        blank=True
    )

    natamam_ay_alt_status = models.CharField(
        max_length=20,
        choices=NATAMAM_STATUS_CHOICES,
        default=None,
        null=True,
        blank=True
    )

    artiq_odeme_alt_status = models.CharField(
        max_length=20,
        choices=ARTIQ_ODEME_STATUS_CHOICES,
        default=None,
        null=True,
        blank=True
    )
    
    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.pk}. {self.tarix} - {self.muqavile} - {self.qiymet}"

class Servis(models.Model):
    kredit = models.BooleanField(default=False, blank=True)
    kredit_muddeti = models.IntegerField(default=0, blank=True)

    muqavile = models.ForeignKey(Muqavile, related_name="servis_muqavile", null=True, on_delete=models.CASCADE)
    mehsullar = models.ManyToManyField(Mehsullar, related_name="servis_mehsul")
    servis_tarix = models.DateField(default=django.utils.timezone.now, blank=True)
    yerine_yetirildi = models.BooleanField(default=False)
    servis_qiymeti = models.FloatField(default=0, blank=True)
    ilkin_odenis = models.FloatField(default=0, blank=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.pk}.servis-{self.muqavile}"

class ServisOdeme(models.Model):
    servis = models.ForeignKey(Servis, related_name="servis_odeme", null=True, on_delete=models.CASCADE)
    servis_qiymeti = models.FloatField(default=0, blank=True)
    endrim = models.FloatField(default=0, blank=True)
    odenilecek_mebleg = models.FloatField(default=0, blank=True)
    qeyd = models.TextField(blank=True)
    odendi = models.BooleanField(default=False)
    odeme_tarix = models.DateField(default=django.utils.timezone.now, blank=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"servis-{self.servis}-{self.odenilecek_mebleg}-{self.odendi}"
