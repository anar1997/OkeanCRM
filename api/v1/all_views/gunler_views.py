from numpy import delete
from api.v1.all_serializers.gunler_serializers import (
    HoldingGunlerSerializer, 
    IsciGunlerSerializer, 
    KomandaGunlerSerializer,
    KomandaIstisnaIsciSerializer, 
    OfisGunlerSerializer,
    OfisIstisnaIsciSerializer, 
    ShirketGunlerSerializer,
    ShirketIstisnaIsciSerializer, 
    ShobeGunlerSerializer,
    ShobeIstisnaIsciSerializer, 
    VezifeGunlerSerializer,
    HoldingIstisnaIsciSerializer,
    VezifeIstisnaIsciSerializer
)
from gunler.models import (
    HoldingGunler,
    IsciGunler,
    KomandaGunler,
    KomandaIstisnaIsci,
    OfisGunler,
    OfisIstisnaIsci,
    ShirketGunler,
    ShirketIstisnaIsci,
    ShobeGunler,
    ShobeIstisnaIsci,
    VezifeGunler,
    HoldingIstisnaIsci,
    VezifeIstisnaIsci
)

import pandas as pd
import datetime

from api.v1.utils import gunler_utils

from rest_framework import status, generics
from rest_framework.generics import get_object_or_404

from rest_framework.response import Response

# ********************************** Holding Gunler get post put delete **********************************
class HoldingGunlerListCreateAPIView(generics.ListAPIView):
    queryset = HoldingGunler.objects.all()
    serializer_class = HoldingGunlerSerializer

class HoldingGunlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HoldingGunler.objects.all()
    serializer_class = HoldingGunlerSerializer

    def update(self, request, *args, **kwargs):
        return gunler_utils.holding_gunler_update(self, request, *args, **kwargs)

class HoldingIstisnaIsciListCreateAPIView(generics.ListCreateAPIView):
    queryset = HoldingIstisnaIsci.objects.all()
    serializer_class = HoldingIstisnaIsciSerializer

    def create(self, request, *args, **kwargs):
        return gunler_utils.holding_istisna_isci_gunler_create(self, request, *args, **kwargs)

class HoldingIstisnaIsciDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HoldingIstisnaIsci.objects.all()
    serializer_class = HoldingIstisnaIsciSerializer

    def update(self, request, *args, **kwargs):
        return gunler_utils.holding_istisna_isci_gunler_update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return gunler_utils.holding_istisna_isci_gunler_delete(self, request, *args, **kwargs)

# ********************************** Shirket Gunler get post put delete **********************************
class ShirketGunlerListCreateAPIView(generics.ListAPIView):
    queryset = ShirketGunler.objects.all()
    serializer_class = ShirketGunlerSerializer


class ShirketGunlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShirketGunler.objects.all()
    serializer_class = ShirketGunlerSerializer

    def update(self, request, *args, **kwargs):
        return gunler_utils.shirket_gunler_update(self, request, *args, **kwargs)

class ShirketIstisnaIsciListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShirketIstisnaIsci.objects.all()
    serializer_class = ShirketIstisnaIsciSerializer

    def create(self, request, *args, **kwargs):
        return gunler_utils.shirket_istisna_isci_gunler_create(self, request, *args, **kwargs)

class ShirketIstisnaIsciDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShirketIstisnaIsci.objects.all()
    serializer_class = ShirketIstisnaIsciSerializer

    def update(self, request, *args, **kwargs):
        return gunler_utils.shirket_istisna_isci_gunler_update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return gunler_utils.shirket_istisna_isci_gunler_delete(self, request, *args, **kwargs)

# ********************************** Ofis Gunler get post put delete **********************************
class OfisGunlerListCreateAPIView(generics.ListAPIView):
    queryset = OfisGunler.objects.all()
    serializer_class = OfisGunlerSerializer


class OfisGunlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfisGunler.objects.all()
    serializer_class = OfisGunlerSerializer

    def update(self, request, *args, **kwargs):
        return gunler_utils.ofis_gunler_update(self, request, *args, **kwargs)

class OfisIstisnaIsciListCreateAPIView(generics.ListCreateAPIView):
    queryset = OfisIstisnaIsci.objects.all()
    serializer_class = OfisIstisnaIsciSerializer

    def create(self, request, *args, **kwargs):
        return gunler_utils.ofis_istisna_isci_gunler_create(self, request, *args, **kwargs)

class OfisIstisnaIsciDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfisIstisnaIsci.objects.all()
    serializer_class = OfisIstisnaIsciSerializer

    def update(self, request, *args, **kwargs):
        return gunler_utils.ofis_istisna_isci_gunler_update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return gunler_utils.ofis_istisna_isci_gunler_delete(self, request, *args, **kwargs)

# ********************************** Shobe Gunler get post put delete **********************************
class ShobeGunlerListCreateAPIView(generics.ListAPIView):
    queryset = ShobeGunler.objects.all()
    serializer_class = ShobeGunlerSerializer


class ShobeGunlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShobeGunler.objects.all()
    serializer_class = ShobeGunlerSerializer

    def update(self, request, *args, **kwargs):
        return gunler_utils.shobe_gunler_update(self, request, *args, **kwargs)

class ShobeIstisnaIsciListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShobeIstisnaIsci.objects.all()
    serializer_class = ShobeIstisnaIsciSerializer

    def create(self, request, *args, **kwargs):
        return gunler_utils.shobe_istisna_isci_gunler_create(self, request, *args, **kwargs)

class ShobeIstisnaIsciDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShobeIstisnaIsci.objects.all()
    serializer_class = ShobeIstisnaIsciSerializer

    def update(self, request, *args, **kwargs):
        return gunler_utils.shobe_istisna_isci_gunler_update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return gunler_utils.shobe_istisna_isci_gunler_delete(self, request, *args, **kwargs)

# ********************************** Komanda Gunler get post put delete **********************************
class KomandaGunlerListCreateAPIView(generics.ListAPIView):
    queryset = KomandaGunler.objects.all()
    serializer_class = KomandaGunlerSerializer


class KomandaGunlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KomandaGunler.objects.all()
    serializer_class = KomandaGunlerSerializer

    def update(self, request, *args, **kwargs):
        return gunler_utils.komanda_gunler_update(self, request, *args, **kwargs)

class KomandaIstisnaIsciListCreateAPIView(generics.ListCreateAPIView):
    queryset = KomandaIstisnaIsci.objects.all()
    serializer_class = KomandaIstisnaIsciSerializer

    def create(self, request, *args, **kwargs):
        return gunler_utils.komanda_istisna_isci_gunler_create(self, request, *args, **kwargs)

class KomandaIstisnaIsciDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KomandaIstisnaIsci.objects.all()
    serializer_class = KomandaIstisnaIsciSerializer

    def update(self, request, *args, **kwargs):
        return gunler_utils.komanda_istisna_isci_gunler_update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return gunler_utils.komanda_istisna_isci_gunler_delete(self, request, *args, **kwargs)

# ********************************** Vezife Gunler get post put delete **********************************
class VezifeGunlerListCreateAPIView(generics.ListAPIView):
    queryset = VezifeGunler.objects.all()
    serializer_class = VezifeGunlerSerializer

class VezifeGunlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VezifeGunler.objects.all()
    serializer_class = VezifeGunlerSerializer

    def update(self, request, *args, **kwargs):
        return gunler_utils.vezife_gunler_update(self, request, *args, **kwargs)

class VezifeIstisnaIsciListCreateAPIView(generics.ListCreateAPIView):
    queryset = VezifeIstisnaIsci.objects.all()
    serializer_class = VezifeIstisnaIsciSerializer

    def create(self, request, *args, **kwargs):
        return gunler_utils.vezife_istisna_isci_gunler_create(self, request, *args, **kwargs)

class VezifeIstisnaIsciDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VezifeIstisnaIsci.objects.all()
    serializer_class = VezifeIstisnaIsciSerializer

    def update(self, request, *args, **kwargs):
        return gunler_utils.vezife_istisna_isci_gunler_update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return gunler_utils.vezife_istisna_isci_gunler_delete(self, request, *args, **kwargs)
    
# ********************************** Isci Gunler get post put delete **********************************
class IsciGunlerListCreateAPIView(generics.ListAPIView):
    queryset = IsciGunler.objects.all()
    serializer_class = IsciGunlerSerializer


class IsciGunlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IsciGunler.objects.all()
    serializer_class = IsciGunlerSerializer

    def update(self, request, *args, **kwargs):
        return gunler_utils.user_gunler_update(self, request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return gunler_utils.user_gunler_patch(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return gunler_utils.user_gunler_delete(self, request, *args, **kwargs)