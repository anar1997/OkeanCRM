import django_filters
from django_filters import DateFromToRangeFilter

from mehsullar.models import (
    Emeliyyat, 
    MuqavileHediyye, 
    Muqavile, 
    OdemeTarix, 
    Anbar, 
    Mehsullar, 
    AnbarQeydler, 
    Servis, 
    Stok
)


class OdemeTarixFilter(django_filters.FilterSet):
    tarix = DateFromToRangeFilter()
    class Meta:
        model = OdemeTarix
        fields = {
            'muqavile' : ['exact'],
            'muqavile__shobe__shobe_adi': ['exact', 'icontains'],
            'muqavile__ofis__ofis_adi': ['exact', 'icontains'],
            'muqavile__shirket__shirket_adi': ['exact', 'icontains'],

            'muqavile__vanleader__asa': ['exact', 'icontains'],
            'muqavile__vanleader__komanda__komanda_adi': ['exact', 'icontains'],
            'muqavile__vanleader__isci_status__status_adi': ['exact', 'icontains'],

            'muqavile__odenis_uslubu': ['exact'],
            'muqavile__kreditor__kreditor__asa': ['exact'],
            'muqavile__muqavile_status': ['exact'],
            'muqavile__muqavile_tarixi': ['exact', 'gte', 'lte'],
            'muqavile__muqavile_umumi_mebleg': ['exact', 'gte', 'lte'],
            'muqavile__mehsul_sayi': ['exact', 'gte', 'lte'],

            'muqavile__musteri__asa': ['exact', 'icontains'],
            'muqavile__musteri__unvan': ['exact', 'icontains'],
            'muqavile__musteri__tel1': ['exact', 'icontains'],
            'muqavile__musteri__tel2': ['exact', 'icontains'],
            'muqavile__musteri__tel3': ['exact', 'icontains'],
            'muqavile__musteri__tel4': ['exact', 'icontains'],

            'tarix': ['exact', 'gte', 'lte'],
            'qiymet': ['exact', 'gte', 'lte'],     
            'odenme_status': ['exact', 'icontains'],
            'gecikdirme_status': ['exact', 'icontains'],
            'buraxilmis_ay_alt_status': ['exact', 'icontains'],
            'natamam_ay_alt_status': ['exact', 'icontains'],
            'artiq_odeme_alt_status': ['exact', 'icontains'],
            'sertli_odeme_status': ['exact', 'icontains'],
            'borcu_bagla_status': ['exact', 'icontains'],
        }


class MuqavileFilter(django_filters.FilterSet):
    class Meta:
        model = Muqavile
        fields = {
            'musteri__asa': ['exact', 'icontains'],
            'musteri__tel1': ['exact', 'icontains'],
            'musteri__tel2': ['exact', 'icontains'],
            'musteri__tel3': ['exact', 'icontains'],
            'musteri__tel4': ['exact', 'icontains'],
            'musteri__bolge__bolge_adi': ['exact', 'icontains'],
            'musteri__bolge': ['exact'],

            'kreditor__kreditor__asa': ['exact'],

            'muqavile_tarixi': ['exact', 'gte', 'lte'],

            'shirket__shirket_adi': ['exact', 'icontains'],
            'ofis__ofis_adi': ['exact', 'icontains'],

            'odenis_uslubu': ['exact', 'icontains'],
            'muqavile_status': ['exact', 'icontains'],
            
            'negd_odenis_1': ['exact', 'gte', 'lte'],
            'negd_odenis_2': ['exact', 'gte', 'lte'],
            'negd_odenis_1_status': ['exact', 'icontains'],
            'negd_odenis_2_status': ['exact', 'icontains'],
            'negd_odenis_1_tarix': ['exact', 'gte', 'lte'],
            'negd_odenis_2_tarix': ['exact', 'gte', 'lte'],

            'yeni_qrafik_mebleg': ['exact', 'gte', 'lte'],
            'yeni_qrafik_status': ['exact', 'icontains'],
            
            'kredit_muddeti': ['exact', 'gte', 'lte'],
            
            'ilkin_odenis': ['exact', 'gte', 'lte'],
            'ilkin_odenis_qaliq': ['exact', 'gte', 'lte'],
            'ilkin_odenis_tarixi': ['exact', 'gte', 'lte'],
            'ilkin_odenis_qaliq_tarixi': ['exact', 'gte', 'lte'],
            'ilkin_odenis_status': ['exact', 'icontains'],
            'qaliq_ilkin_odenis_status': ['exact', 'icontains'],

            'vanleader__komanda': ['exact'],
            'vanleader__komanda__komanda_adi': ['exact', 'icontains'],
            'vanleader__asa': ['exact', 'icontains'],
            'vanleader__isci_status__status_adi': ['exact', 'icontains'],

            'dealer__asa': ['exact', 'icontains'],
            'dealer__isci_status__status_adi': ['exact', 'icontains'],

            'canvesser__asa': ['exact', 'icontains'],
            'canvesser__isci_status__status_adi': ['exact', 'icontains'],

            'mehsul_sayi': ['exact', 'gte', 'lte'],
            'mehsul__mehsulun_adi': ['exact', 'icontains'],
            'mehsul__qiymet': ['exact', 'gte', 'lte'],

            'muqavile_umumi_mebleg': ['exact', 'gte', 'lte'],

            'kompensasiya_medaxil': ['exact', 'gte', 'lte'],
            'kompensasiya_mexaric': ['exact', 'gte', 'lte']
        }


class StokFilter(django_filters.FilterSet):
    class Meta:
        model = Stok
        fields = {
            'mehsul__id': ['exact'],
            'mehsul__mehsulun_adi': ['exact', 'icontains'],
            'mehsul__qiymet': ['exact', 'gte', 'lte'],

            'anbar__shirket__shirket_adi': ['exact', 'icontains'],
            'anbar__ofis__ofis_adi': ['exact', 'icontains'],
            'anbar__ad': ['exact', 'icontains'],
        }

class EmeliyyatFilter(django_filters.FilterSet):
    class Meta:
        model = Emeliyyat
        fields = {
            'mehsulun_sayi': ['exact', 'gte', 'lte'],

            'gonderen__ad': ['exact', 'icontains'],
            'gonderen__ofis__ofis_adi': ['exact', 'icontains'],
            'gonderen__shirket__shirket_adi': ['exact', 'icontains'],

            'qebul_eden__ad': ['exact', 'icontains'],
            'qebul_eden__ofis__ofis_adi': ['exact', 'icontains'],
            'qebul_eden__shirket__shirket_adi': ['exact', 'icontains'],

            'gonderilen_mehsul__mehsulun_adi': ['exact', 'icontains'],
            'gonderilen_mehsul__qiymet': ['exact', 'gte', 'lte'],
            'gonderilen_mehsul__shirket__shirket_adi': ['exact', 'icontains'],
            
            'qeyd': ['exact', 'icontains'],

            'emeliyyat_tarixi': ['exact', 'gte', 'lte'],
        }

class MuqavileHediyyeFilter(django_filters.FilterSet):
    class Meta:
        model = MuqavileHediyye
        fields = {
            'mehsul__id': ['exact'],
            'mehsul__mehsulun_adi': ['exact', 'icontains'],
            'mehsul__qiymet': ['exact', 'gte', 'lte'],

            'muqavile' : ['exact'],
            'muqavile__shobe__shobe_adi': ['exact', 'icontains'],
            'muqavile__ofis__ofis_adi': ['exact', 'icontains'],
            'muqavile__shirket__shirket_adi': ['exact', 'icontains'],

            'muqavile__vanleader__asa': ['exact', 'icontains'],
            'muqavile__vanleader__komanda__komanda_adi': ['exact', 'icontains'],
            'muqavile__vanleader__isci_status__status_adi': ['exact', 'icontains'],


            'muqavile__odenis_uslubu': ['exact'],
            'muqavile__muqavile_status': ['exact'],
            'muqavile__muqavile_tarixi': ['exact', 'gte', 'lte'],
            'muqavile__muqavile_umumi_mebleg': ['exact', 'gte', 'lte'],
            'muqavile__mehsul_sayi': ['exact', 'gte', 'lte'],

            'muqavile__musteri__asa': ['exact', 'icontains'],
            'muqavile__musteri__unvan': ['exact', 'icontains'],
            'muqavile__musteri__tel1': ['exact', 'icontains'],
            'muqavile__musteri__tel2': ['exact', 'icontains'],
            'muqavile__musteri__tel3': ['exact', 'icontains'],
            'muqavile__musteri__tel4': ['exact', 'icontains'],
        }

class AnbarFilter(django_filters.FilterSet):
    class Meta:
        model = Anbar
        fields = {
            'ad': ['exact', 'icontains'],
            'ofis__ofis_adi': ['exact', 'icontains'],
            'ofis__shirket__shirket_adi': ['exact', 'icontains'],
        }

class AnbarQeydlerFilter(django_filters.FilterSet):
    class Meta:
        model = AnbarQeydler
        fields = {
            'qeyd': ['exact', 'icontains'],
            'anbar__ad': ['exact', 'icontains'],
            'anbar__ofis__ofis_adi': ['exact', 'icontains'],
        }


class MehsullarFilter(django_filters.FilterSet):
    class Meta:
        model = Mehsullar
        fields = {
            'mehsulun_adi': ['exact', 'icontains'],
            'qiymet': ['exact', 'gte', 'lte'],
            'shirket__shirket_adi': ['exact', 'icontains'],
            'is_hediyye': ['exact'],
        }

class ServisFilter(django_filters.FilterSet):
    pass
    # class Meta:
    #     model = Servis
    #     fields = {
    #         'muqavile' : ['exact'],
    #         'muqavile__shobe__shobe_adi': ['exact', 'icontains'],
    #         'muqavile__ofis__ofis_adi': ['exact', 'icontains'],
    #         'muqavile__shirket__shirket_adi': ['exact', 'icontains'],

    #         'kreditor__kreditor__asa': ['exact'],

    #         'muqavile__vanleader__asa': ['exact', 'icontains'],
    #         'muqavile__vanleader__komanda__komanda_adi': ['exact', 'icontains'],
    #         'muqavile__vanleader__isci_status__status_adi': ['exact', 'icontains'],

    #         'muqavile__odenis_uslubu': ['exact'],
    #         'muqavile__muqavile_status': ['exact'],
    #         'muqavile__muqavile_tarixi': ['exact', 'gte', 'lte'],
    #         'muqavile__muqavile_umumi_mebleg': ['exact', 'gte', 'lte'],
    #         'muqavile__mehsul_sayi': ['exact', 'gte', 'lte'],

    #         'muqavile__musteri__asa': ['exact', 'icontains'],
    #         'muqavile__musteri__unvan': ['exact', 'icontains'],
    #         'muqavile__musteri__tel1': ['exact', 'icontains'],
    #         'muqavile__musteri__tel2': ['exact', 'icontains'],
    #         'muqavile__musteri__tel3': ['exact', 'icontains'],
    #         'muqavile__musteri__tel4': ['exact', 'icontains'],

    #         'kartric1__mehsulun_adi': ['exact', 'icontains'],
    #         'kartric1__qiymet': ['exact', 'gte', 'lte'],
    #         'kartric1__shirket__shirket_adi': ['exact', 'icontains'],
    #         'kartric1__is_hediyye': ['exact'],

    #         'kartric2__mehsulun_adi': ['exact', 'icontains'],
    #         'kartric2__qiymet': ['exact', 'gte', 'lte'],
    #         'kartric2__shirket__shirket_adi': ['exact', 'icontains'],
    #         'kartric2__is_hediyye': ['exact'],

    #         'kartric3__mehsulun_adi': ['exact', 'icontains'],
    #         'kartric3__qiymet': ['exact', 'gte', 'lte'],
    #         'kartric3__shirket__shirket_adi': ['exact', 'icontains'],
    #         'kartric3__is_hediyye': ['exact'],

    #         'kartric4__mehsulun_adi': ['exact', 'icontains'],
    #         'kartric4__qiymet': ['exact', 'gte', 'lte'],
    #         'kartric4__shirket__shirket_adi': ['exact', 'icontains'],
    #         'kartric4__is_hediyye': ['exact'],

    #         'kartric5__mehsulun_adi': ['exact', 'icontains'],
    #         'kartric5__qiymet': ['exact', 'gte', 'lte'],
    #         'kartric5__shirket__shirket_adi': ['exact', 'icontains'],
    #         'kartric5__is_hediyye': ['exact'],

    #         'kartric6__mehsulun_adi': ['exact', 'icontains'],
    #         'kartric6__qiymet': ['exact', 'gte', 'lte'],
    #         'kartric6__shirket__shirket_adi': ['exact', 'icontains'],
    #         'kartric6__is_hediyye': ['exact'],

    #         'servis_tarix6ay': ['exact', 'gte', 'lte'],
    #         'servis_tarix18ay': ['exact', 'gte', 'lte'],
    #         'servis_tarix24ay': ['exact', 'gte', 'lte'],
    #     }