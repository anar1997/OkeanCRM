from rest_framework import status, permissions, generics

import math
import pandas as pd

import datetime

from rest_framework.response import Response
from rest_framework import generics

from api.v1.all_serializers.muqavile_serializers import (
    AnbarSerializer,
    MehsullarSerializer,
    EmeliyyatSerializer,
    AnbarQeydlerSerializer,
    MuqavileSerializer,
    MuqavileHediyyeSerializer,
    OdemeTarixSerializer,
    ServisOdemeSerializer,
    ServisSerializer,
    StokSerializer,
)

from mehsullar.models import (
    Emeliyyat, 
    MuqavileHediyye, 
    Muqavile, 
    OdemeTarix, 
    Anbar, 
    Mehsullar, 
    AnbarQeydler, 
    Servis,
    ServisOdeme, 
    Stok
)
from api.v1.utils import (
    odeme_tarixleri_utils,
    muqavile_utils,
    muqavile_hediyye_utils,
    anbar_emeliyyat_utils,
    servis_utils,
    stok_utils
)

from django_filters.rest_framework import DjangoFilterBackend

from api.v1.filters.muqavile_filters.filters import (
    AnbarFilter,
    AnbarQeydlerFilter,
    EmeliyyatFilter,
    MehsullarFilter,
    MuqavileHediyyeFilter,
    OdemeTarixFilter,
    MuqavileFilter,
    ServisFilter,
    StokFilter,
)

from rest_framework.generics import get_object_or_404

from api.v1.permissions.muqavile_permissions import permissions as muqavile_permissions

# ********************************** muqavile get post put delete **********************************

class MuqavileListCreateAPIView(generics.ListCreateAPIView):
    queryset = Muqavile.objects.all()
    serializer_class = MuqavileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MuqavileFilter
    permission_classes = [muqavile_permissions.MuqavilePermissions]

    def create(self, request, *args, **kwargs):
        return muqavile_utils.muqavile_create(self, request, *args, **kwargs)


class MuqavileDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Muqavile.objects.all()
    serializer_class = MuqavileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MuqavileFilter
    permission_classes = [muqavile_permissions.MuqavilePermissions]

    def patch(self, request, *args, **kwargs):
        return muqavile_utils.muqavile_patch(self, request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return muqavile_utils.muqavile_update(self, request, *args, **kwargs)


# ********************************** odeme tarixi put get post delete **********************************


class OdemeTarixListCreateAPIView(generics.ListCreateAPIView):
    queryset = OdemeTarix.objects.all()
    serializer_class = OdemeTarixSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OdemeTarixFilter
    permission_classes = [muqavile_permissions.OdemeTarixleriPermissions]

class OdemeTarixDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = OdemeTarix.objects.all()
    serializer_class = OdemeTarixSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['muqavile']
    filterset_class = OdemeTarixFilter
    permission_classes = [muqavile_permissions.OdemeTarixleriPermissions]


    # PATCH SORGUSU
    def patch(self, request, *args, **kwargs):
        return odeme_tarixleri_utils.odeme_tarixi_patch(self, request, *args, **kwargs)

    # PUT SORGUSU
    def update(self, request, *args, **kwargs):
        return odeme_tarixleri_utils.odeme_tarixi_update(self, request, *args, **kwargs)


# ********************************** anbar put get post delete **********************************


class AnbarListCreateAPIView(generics.ListCreateAPIView):
    queryset = Anbar.objects.all()
    serializer_class = AnbarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AnbarFilter
    permission_classes = [muqavile_permissions.AnbarPermissions]


class AnbarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anbar.objects.all()
    serializer_class = AnbarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AnbarFilter
    permission_classes = [muqavile_permissions.AnbarPermissions]


# ********************************** mehsullar put get post delete **********************************


class MehsullarListCreateAPIView(generics.ListCreateAPIView):
    queryset = Mehsullar.objects.all()
    serializer_class = MehsullarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MehsullarFilter
    permission_classes = [muqavile_permissions.MehsullarPermissions]


class MehsullarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mehsullar.objects.all()
    serializer_class = MehsullarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MehsullarFilter
    permission_classes = [muqavile_permissions.MehsullarPermissions]


# ********************************** anbar put delete post get **********************************


class AnbarQeydlerListCreateAPIView(generics.ListCreateAPIView):
    queryset = AnbarQeydler.objects.all()
    serializer_class = AnbarQeydlerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AnbarQeydlerFilter
    permission_classes = [muqavile_permissions.AnbarQeydlerPermissions]


class AnbarQeydlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnbarQeydler.objects.all()
    serializer_class = AnbarQeydlerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AnbarQeydlerFilter
    permission_classes = [muqavile_permissions.AnbarQeydlerPermissions]

# ********************************** emeliyyat put delete post get **********************************


class EmeliyyatListCreateAPIView(generics.ListCreateAPIView):
    queryset = Emeliyyat.objects.all()
    serializer_class = EmeliyyatSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmeliyyatFilter
    permission_classes = [muqavile_permissions.EmeliyyatPermissions]

    def create(self, request, *args, **kwargs):
        return anbar_emeliyyat_utils.emeliyyat_create(self, request, *args, **kwargs)

class EmeliyyatDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Emeliyyat.objects.all()
    serializer_class = EmeliyyatSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmeliyyatFilter
    permission_classes = [muqavile_permissions.EmeliyyatPermissions]


# ********************************** hediyye put delete post get **********************************


class MuqavileHediyyeListCreateAPIView(generics.ListCreateAPIView):
    queryset = MuqavileHediyye.objects.all()
    serializer_class = MuqavileHediyyeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MuqavileHediyyeFilter
    permission_classes = [muqavile_permissions.MuqavileHediyyePermissions]

    def create(self, request, *args, **kwargs):
        return muqavile_hediyye_utils.muqavile_hediyye_create(self, request, *args, **kwargs)


class MuqavileHediyyeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MuqavileHediyye.objects.all()
    serializer_class = MuqavileHediyyeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MuqavileHediyyeFilter
    permission_classes = [muqavile_permissions.MuqavileHediyyePermissions]

    def destroy(self, request, *args, **kwargs):
        return muqavile_hediyye_utils.muqavile_hediyye_destroy(self, request, *args, **kwargs)


# ********************************** servis put delete post get **********************************

class ServisListCreateAPIView(generics.ListCreateAPIView):
    queryset = Servis.objects.all()
    serializer_class = ServisSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ServisFilter
    permission_classes = [muqavile_permissions.ServisPermissions]

class ServisDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servis.objects.all()
    serializer_class = ServisSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ServisFilter
    permission_classes = [muqavile_permissions.ServisPermissions]

    def update(self, request, *args, **kwargs):
        return servis_utils.servis_update(self, request, *args, **kwargs)

# ********************************** servis odeme put delete post get **********************************

class ServisOdemeListCreateAPIView(generics.ListCreateAPIView):
    queryset = ServisOdeme.objects.all()
    serializer_class = ServisOdemeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ServisFilter
    permission_classes = [muqavile_permissions.ServisPermissions]

class ServisOdemeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServisOdeme.objects.all()
    serializer_class = ServisOdemeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ServisFilter
    permission_classes = [muqavile_permissions.ServisPermissions]

    def update(self, request, *args, **kwargs):
        return servis_utils.servis_odeme_update(self, request, *args, **kwargs)

# ********************************** stok put delete post get **********************************

class StokListCreateAPIView(generics.ListCreateAPIView):
    queryset = Stok.objects.all()
    serializer_class = StokSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StokFilter
    permission_classes = [muqavile_permissions.StokPermissions]


class StokDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stok.objects.all()
    serializer_class = StokSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StokFilter
    permission_classes = [muqavile_permissions.StokPermissions]

    def update(self, request, *args, **kwargs):
        return stok_utils.stok_update(self, request, *args, **kwargs)