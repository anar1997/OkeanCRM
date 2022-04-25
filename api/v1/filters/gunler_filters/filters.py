import django_filters

from gunler.models import (
    HoldingGunler,
    IsciGelibGetmeVaxtlari,
    IsciGunler,
    KomandaGunler,
    KomandaIstisnaIsci,
    OfisGunler,
    OfisIstisnaIsci,
    ShirketGunler,
    ShirketIstisnaIsci,
    ShobeGunler,
    VezifeGunler,
    HoldingIstisnaIsci,
    VezifeIstisnaIsci,
    ShobeIstisnaIsci
)

class IsciGelibGetmeVaxtlariFilter(django_filters.FilterSet):
    class Meta:
        model = IsciGelibGetmeVaxtlari
        fields = {
            'isci__asa': ['exact', 'icontains'],
            'gelme_vaxti': ['exact', 'gte', 'lte'],
            'getme_vaxti': ['exact', 'gte', 'lte'],
        }

class IsciGunlerFilter(django_filters.FilterSet):
    class Meta:
        model = IsciGunler
        fields = {
            'isci__asa': ['exact', 'icontains'],
            'is_gunleri_count': ['exact', 'gte', 'lte'],
            'qeyri_is_gunu_count': ['exact', 'gte', 'lte'],
            'tetil_gunleri': ['exact', 'icontains'],
            'icaze_gunleri_odenisli': ['exact', 'icontains'],
            'icaze_gunleri_odenissiz': ['exact', 'icontains'],
            'tarix': ['exact', 'gte', 'lte'],
        }

class HoldingGunlerFilter(django_filters.FilterSet):
    class Meta:
        model = HoldingGunler
        fields = {
            'holding__holding_adi': ['exact', 'icontains'],
            'is_gunleri_count': ['exact', 'gte', 'lte'],
            'qeyri_is_gunu_count': ['exact', 'gte', 'lte'],
            'tetil_gunleri': ['exact', 'icontains'],
            'tarix': ['exact', 'gte', 'lte'],
        }

class ShirketGunlerFilter(django_filters.FilterSet):
    class Meta:
        model = ShirketGunler
        fields = {
            'shirket__shirket_adi': ['exact', 'icontains'],
            'is_gunleri_count': ['exact', 'gte', 'lte'],
            'qeyri_is_gunu_count': ['exact', 'gte', 'lte'],
            'tetil_gunleri': ['exact', 'icontains'],
            'tarix': ['exact', 'gte', 'lte'],
        }

class OfisGunlerFilter(django_filters.FilterSet):
    class Meta:
        model = OfisGunler
        fields = {
            'ofis__ofis_adi': ['exact', 'icontains'],
            'is_gunleri_count': ['exact', 'gte', 'lte'],
            'qeyri_is_gunu_count': ['exact', 'gte', 'lte'],
            'tetil_gunleri': ['exact', 'icontains'],
            'tarix': ['exact', 'gte', 'lte'],
        }

class ShobeGunlerFilter(django_filters.FilterSet):
    class Meta:
        model = ShobeGunler
        fields = {
            'shobe__shobe_adi': ['exact', 'icontains'],
            'is_gunleri_count': ['exact', 'gte', 'lte'],
            'qeyri_is_gunu_count': ['exact', 'gte', 'lte'],
            'tetil_gunleri': ['exact', 'icontains'],
            'tarix': ['exact', 'gte', 'lte'],
        }


class KomandaGunlerFilter(django_filters.FilterSet):
    class Meta:
        model = KomandaGunler
        fields = {
            'komanda__komanda_adi': ['exact', 'icontains'],
            'is_gunleri_count': ['exact', 'gte', 'lte'],
            'qeyri_is_gunu_count': ['exact', 'gte', 'lte'],
            'tetil_gunleri': ['exact', 'icontains'],
            'tarix': ['exact', 'gte', 'lte'],
        }

class VezifeGunlerFilter(django_filters.FilterSet):
    class Meta:
        model = VezifeGunler
        fields = {
            'vezife__vezife_adi': ['exact', 'icontains'],
            'is_gunleri_count': ['exact', 'gte', 'lte'],
            'qeyri_is_gunu_count': ['exact', 'gte', 'lte'],
            'tetil_gunleri': ['exact', 'icontains'],
            'tarix': ['exact', 'gte', 'lte'],
        }

class KomandaIstisnaIsciFilter(django_filters.FilterSet):
    class Meta:
        model = KomandaIstisnaIsci
        fields = {
            'komanda_gunler__komanda__komanda_adi': ['exact', 'icontains'],
            'komanda_gunler__is_gunleri_count': ['exact', 'gte', 'lte'],
            'komanda_gunler__qeyri_is_gunu_count': ['exact', 'gte', 'lte'],
            'komanda_gunler__tetil_gunleri': ['exact', 'icontains'],
            'komanda_gunler__tarix': ['exact', 'gte', 'lte'],
        }

class OfisIstisnaIsciFilter(django_filters.FilterSet):
    class Meta:
        model = OfisIstisnaIsci
        fields = {
            'ofis_gunler__ofis__ofis_adi': ['exact', 'icontains'],
            'ofis_gunler__is_gunleri_count': ['exact', 'gte', 'lte'],
            'ofis_gunler__qeyri_is_gunu_count': ['exact', 'gte', 'lte'],
            'ofis_gunler__tetil_gunleri': ['exact', 'icontains'],
            'ofis_gunler__tarix': ['exact', 'gte', 'lte'],
        }

class ShirketIstisnaIsciFilter(django_filters.FilterSet):
    class Meta:
        model = ShirketIstisnaIsci
        fields = {
            'shirket_gunler__shirket__shirket_adi': ['exact', 'icontains'],
            'shirket_gunler__is_gunleri_count': ['exact', 'gte', 'lte'],
            'shirket_gunler__qeyri_is_gunu_count': ['exact', 'gte', 'lte'],
            'shirket_gunler__tetil_gunleri': ['exact', 'icontains'],
            'shirket_gunler__tarix': ['exact', 'gte', 'lte'],
        }

class HoldingIstisnaIsciFilter(django_filters.FilterSet):
    class Meta:
        model = HoldingIstisnaIsci
        fields = {
            'holding_gunler__holding__holding_adi': ['exact', 'icontains'],
            'holding_gunler__is_gunleri_count': ['exact', 'gte', 'lte'],
            'holding_gunler__qeyri_is_gunu_count': ['exact', 'gte', 'lte'],
            'holding_gunler__tetil_gunleri': ['exact', 'icontains'],
            'holding_gunler__tarix': ['exact', 'gte', 'lte'],
        }

class VezifeIstisnaIsciFilter(django_filters.FilterSet):
    class Meta:
        model = VezifeIstisnaIsci
        fields = {
            'vezife_gunler__vezife__vezife_adi': ['exact', 'icontains'],
            'vezife_gunler__is_gunleri_count': ['exact', 'gte', 'lte'],
            'vezife_gunler__qeyri_is_gunu_count': ['exact', 'gte', 'lte'],
            'vezife_gunler__tetil_gunleri': ['exact', 'icontains'],
            'vezife_gunler__tarix': ['exact', 'gte', 'lte'],
        }

class ShobeIstisnaIsciFilter(django_filters.FilterSet):
    class Meta:
        model = ShobeIstisnaIsci
        fields = {
            'shobe_gunler__shobe__shobe_adi': ['exact', 'icontains'],
            'shobe_gunler__shobe__shobe_adi': ['exact', 'icontains'],
            'shobe_gunler__is_gunleri_count': ['exact', 'gte', 'lte'],
            'shobe_gunler__qeyri_is_gunu_count': ['exact', 'gte', 'lte'],
            'shobe_gunler__tetil_gunleri': ['exact', 'icontains'],
            'shobe_gunler__tarix': ['exact', 'gte', 'lte'],
        }