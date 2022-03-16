import django_filters
from django_filters import DateFromToRangeFilter

from mehsullar.models import OdemeTarix, Muqavile, Stok


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
            'muqavile__odenis_uslubu': ['exact'],
            'muqavile__muqavile_status': ['exact'],

            'muqavile__musteri__asa': ['exact', 'icontains'],
            'muqavile__musteri__unvan': ['exact', 'icontains'],
            'muqavile__musteri__tel1': ['exact', 'icontains'],
            'muqavile__musteri__tel2': ['exact', 'icontains'],
            'muqavile__musteri__tel3': ['exact', 'icontains'],
            'muqavile__musteri__tel4': ['exact', 'icontains'],

            'tarix': ['exact', 'gte', 'lte'],
            'qiymet': ['exact', 'gte', 'lte'],     
            'odenme_status': ['exact'],
            'gecikdirme_status': ['exact'],
            'buraxilmis_ay_alt_status': ['exact'],
            'natamam_ay_alt_status': ['exact'],
            'artiq_odeme_alt_status': ['exact'],
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
            'muqavile_tarixi': ['exact', 'gte', 'lte'],
            'shirket__shirket_adi': ['exact', 'icontains'],
            'ofis__ofis_adi': ['exact', 'icontains'],
            'odenis_uslubu': ['exact', 'icontains'],
            'muqavile_status': ['exact', 'icontains'],
            'negd_odenis_1_status': ['exact', 'icontains'],
            'negd_odenis_2_status': ['exact', 'icontains'],
            'kredit_muddeti': ['exact'],
            'ilkin_odenis_tarixi': ['exact', 'gte', 'lte'],
            'ilkin_odenis_qaliq_tarixi': ['exact', 'gte', 'lte'],
            'ilkin_odenis_status': ['exact', 'icontains'],
            'qaliq_ilkin_odenis_status': ['exact', 'icontains'],

            'vanleader__komanda__komanda_adi': ['exact', 'icontains'],
        }


class StokFilter(django_filters.FilterSet):
    class Meta:
        model = Stok
        fields = {
            'mehsul__id': ['exact'],
            'mehsul__mehsulun_adi': ['exact', 'icontains'],
            'anbar__shirket__shirket_adi': ['exact', 'icontains'],
            'anbar__ad': ['exact', 'icontains'],
            'mehsul__qiymet': ['exact'],
        }