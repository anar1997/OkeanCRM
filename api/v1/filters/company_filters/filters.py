import django_filters

from company.models import (
    Holding,
    HoldingKassa,
    HoldingKassaMedaxil,
    HoldingKassaMexaric,
    HoldingdenShirketlereTransfer,
    OfisKassaMedaxil,
    OfisKassaMexaric,

    Shirket,
    ShirketKassa,
    ShirketKassaMedaxil,
    ShirketKassaMexaric,
    ShirketdenHoldingeTransfer,
    ShirketdenOfislereTransfer,

    Ofis,
    OfisKassa,
    OfisdenShirketeTransfer,

    Komanda,
    Shobe,
    Vezifeler
)

class ShirketFilter(django_filters.FilterSet):
    class Meta:
        model = Shirket
        fields = {
            'shirket_adi': ['exact', 'icontains'],
        }

class OfisFilter(django_filters.FilterSet):
    class Meta:
        model = Ofis
        fields = {
            'ofis_adi': ['exact', 'icontains'],
            'shirket__shirket_adi': ['exact', 'icontains'],
        }

class ShobeFilter(django_filters.FilterSet):
    class Meta:
        model = Shobe
        fields = {
            'shobe_adi': ['exact', 'icontains'],
            'ofis__ofis_adi': ['exact', 'icontains'],
        }

class VezifeFilter(django_filters.FilterSet):
    class Meta:
        model = Vezifeler
        fields = {
            'vezife_adi': ['exact', 'icontains'],
            'shirket__shirket_adi': ['exact', 'icontains'],
            'shobe__shobe_adi': ['exact', 'icontains'],
        }

class KomandaFilter(django_filters.FilterSet):
    class Meta:
        model = Komanda
        fields = {
            'komanda_adi': ['exact', 'icontains'],
            'is_active': ['exact']
        }

class HoldingKassaFilter(django_filters.FilterSet):
    class Meta:
        model = HoldingKassa
        fields = {
            'holding__holding_adi': ['exact', 'icontains'],
            'balans': ['exact', 'gte', 'lte'],
        }

class ShirketKassaFilter(django_filters.FilterSet):
    class Meta:
        model = ShirketKassa
        fields = {
            'shirket__shirket_adi': ['exact', 'icontains'],
            'balans': ['exact', 'gte', 'lte'],
        }

class OfisKassaFilter(django_filters.FilterSet):
    class Meta:
        model = OfisKassa
        fields = {
            'ofis__ofis_adi': ['exact', 'icontains'],
            'balans': ['exact', 'gte', 'lte'],
        }

class HoldingKassaMedaxilFilter(django_filters.FilterSet):
    class Meta:
        model = HoldingKassaMedaxil
        fields = {
            'medaxil_eden__asa': ['exact', 'icontains'],
            'medaxil_eden__vezife__vezife_adi': ['exact', 'icontains'],
            'medaxil_eden__isci_status__status_adi': ['exact', 'icontains'],

            'holding_kassa__holding__holding_adi': ['exact', 'icontains'],
            'mebleg': ['exact', 'gte', 'lte'],
            'qeyd': ['exact', 'icontains'],
            
            'medaxil_tarixi': ['exact', 'gte', 'lte'],

        }

class HoldingKassaMexaricFilter(django_filters.FilterSet):
    class Meta:
        model = HoldingKassaMexaric
        fields = {
            'mexaric_eden__asa': ['exact', 'icontains'],
            'mexaric_eden__vezife__vezife_adi': ['exact', 'icontains'],
            'mexaric_eden__isci_status__status_adi': ['exact', 'icontains'],

            'holding_kassa__holding__holding_adi': ['exact', 'icontains'],
            'mebleg': ['exact', 'gte', 'lte'],
            'qeyd': ['exact', 'icontains'],
            
            'mexaric_tarixi': ['exact', 'gte', 'lte'],
        }

class ShirketKassaMedaxilFilter(django_filters.FilterSet):
    class Meta:
        model = ShirketKassaMedaxil
        fields = {
            'medaxil_eden__asa': ['exact', 'icontains'],
            'medaxil_eden__vezife__vezife_adi': ['exact', 'icontains'],
            'medaxil_eden__isci_status__status_adi': ['exact', 'icontains'],

            'shirket_kassa__shirket__shirket_adi': ['exact', 'icontains'],
            'mebleg': ['exact', 'gte', 'lte'],
            'qeyd': ['exact', 'icontains'],
            
            'medaxil_tarixi': ['exact', 'gte', 'lte'],

        }

class ShirketKassaMexaricFilter(django_filters.FilterSet):
    class Meta:
        model = ShirketKassaMexaric
        fields = {
            'mexaric_eden__asa': ['exact', 'icontains'],
            'mexaric_eden__vezife__vezife_adi': ['exact', 'icontains'],
            'mexaric_eden__isci_status__status_adi': ['exact', 'icontains'],

            'shirket_kassa__shirket__shirket_adi': ['exact', 'icontains'],
            'mebleg': ['exact', 'gte', 'lte'],
            'qeyd': ['exact', 'icontains'],
            
            'mexaric_tarixi': ['exact', 'gte', 'lte'],
        }

class OfisKassaMedaxilFilter(django_filters.FilterSet):
    class Meta:
        model = OfisKassaMedaxil
        fields = {
            'medaxil_eden__asa': ['exact', 'icontains'],
            'medaxil_eden__vezife__vezife_adi': ['exact', 'icontains'],
            'medaxil_eden__isci_status__status_adi': ['exact', 'icontains'],

            'ofis_kassa__ofis__ofis_adi': ['exact', 'icontains'],
            'mebleg': ['exact', 'gte', 'lte'],
            'qeyd': ['exact', 'icontains'],
            
            'medaxil_tarixi': ['exact', 'gte', 'lte'],

        }

class OfisKassaMexaricFilter(django_filters.FilterSet):
    class Meta:
        model = OfisKassaMexaric
        fields = {
            'mexaric_eden__asa': ['exact', 'icontains'],
            'mexaric_eden__vezife__vezife_adi': ['exact', 'icontains'],
            'mexaric_eden__isci_status__status_adi': ['exact', 'icontains'],

            'ofis_kassa__ofis__ofis_adi': ['exact', 'icontains'],
            'mebleg': ['exact', 'gte', 'lte'],
            'qeyd': ['exact', 'icontains'],
            
            'mexaric_tarixi': ['exact', 'gte', 'lte'],
        }

class HoldingdenShirketlereTransferFilter(django_filters.FilterSet):
    class Meta:
        model = HoldingdenShirketlereTransfer
        fields = {
            'transfer_eden__asa': ['exact', 'icontains'],
            'transfer_eden__vezife__vezife_adi': ['exact', 'icontains'],
            'transfer_eden__isci_status__status_adi': ['exact', 'icontains'],

            'holding_kassa__holding__holding_adi': ['exact', 'icontains'],
            'shirket_kassa__shirket__shirket_adi': ['exact', 'icontains'],

            'transfer_meblegi': ['exact', 'gte', 'lte'],
            'transfer_qeydi': ['exact', 'icontains'],
            
            'transfer_tarixi': ['exact', 'gte', 'lte'],
        }


class ShirketdenHoldingeTransferFilter(django_filters.FilterSet):
    class Meta:
        model = ShirketdenHoldingeTransfer
        fields = {
            'transfer_eden__asa': ['exact', 'icontains'],
            'transfer_eden__vezife__vezife_adi': ['exact', 'icontains'],
            'transfer_eden__isci_status__status_adi': ['exact', 'icontains'],

            'holding_kassa__holding__holding_adi': ['exact', 'icontains'],
            'shirket_kassa__shirket__shirket_adi': ['exact', 'icontains'],

            'transfer_meblegi': ['exact', 'gte', 'lte'],
            'transfer_qeydi': ['exact', 'icontains'],
            
            'transfer_tarixi': ['exact', 'gte', 'lte'],
        }

class ShirketdenOfislereTransferFilter(django_filters.FilterSet):
    class Meta:
        model = ShirketdenOfislereTransfer
        fields = {
            'transfer_eden__asa': ['exact', 'icontains'],
            'transfer_eden__vezife__vezife_adi': ['exact', 'icontains'],
            'transfer_eden__isci_status__status_adi': ['exact', 'icontains'],

            'ofis_kassa__ofis__ofis_adi': ['exact', 'icontains'],
            'shirket_kassa__shirket__shirket_adi': ['exact', 'icontains'],

            'transfer_meblegi': ['exact', 'gte', 'lte'],
            'transfer_qeydi': ['exact', 'icontains'],
            
            'transfer_tarixi': ['exact', 'gte', 'lte'],
        }

class OfisdenShirketeTransferFilter(django_filters.FilterSet):
    class Meta:
        model = OfisdenShirketeTransfer
        fields = {
            'transfer_eden__asa': ['exact', 'icontains'],
            'transfer_eden__vezife__vezife_adi': ['exact', 'icontains'],
            'transfer_eden__isci_status__status_adi': ['exact', 'icontains'],

            'ofis_kassa__ofis__ofis_adi': ['exact', 'icontains'],
            'shirket_kassa__shirket__shirket_adi': ['exact', 'icontains'],

            'transfer_meblegi': ['exact', 'gte', 'lte'],
            'transfer_qeydi': ['exact', 'icontains'],
            
            'transfer_tarixi': ['exact', 'gte', 'lte'],
        }