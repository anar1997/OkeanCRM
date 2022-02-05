import django_filters
from mehsullar.models import Dates, Muqavile

class DatesFilter(django_filters.FilterSet):
    class Meta:
        model = Dates
        fields = {
            'muqavile__shobe__shobe_adi':['icontains']
        }

class MuqavileFilter(django_filters.FilterSet):

    class Meta:
        model = Muqavile
        fields = {
            'musteri__asa':['exact', 'icontains'],
            'musteri__tel1':['exact', 'icontains'],
            'musteri__tel2':['exact', 'icontains'],
            'musteri__tel3':['exact', 'icontains'],
            'musteri__tel4':['exact', 'icontains']
        }