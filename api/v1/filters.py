import django_filters
from django_filters import DateFromToRangeFilter

from mehsullar.models import OdemeTarix, Muqavile


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

            'tarix': ['exact'],
            'odenme_status': ['exact'],
            'gecikdirme_status': ['exact'],
        }


class MuqavileFilter(django_filters.FilterSet):
    class Meta:
        model = Muqavile
        fields = {
            'musteri__asa': ['exact', 'icontains'],
            'musteri__tel1': ['exact', 'icontains'],
            'musteri__tel2': ['exact', 'icontains'],
            'musteri__tel3': ['exact', 'icontains'],
            'musteri__tel4': ['exact', 'icontains']
        }
