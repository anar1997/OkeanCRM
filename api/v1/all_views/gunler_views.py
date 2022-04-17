from numpy import delete
from api.v1.all_serializers.gunler_serializers import (
    HoldingGunlerSerializer,
    IsciGelibGetmeVaxtlariSerializer, 
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
    IsciGelibGetmeVaxtlari,
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
from api.v1.permissions.gunler_permissions import permissions as gunler_permissions

# ********************************** Holding Gunler get post put delete **********************************
class HoldingGunlerListCreateAPIView(generics.ListAPIView):
    queryset = HoldingGunler.objects.all()
    serializer_class = HoldingGunlerSerializer
    permission_classes = [gunler_permissions.HoldingGunlerPermissions]

class HoldingGunlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HoldingGunler.objects.all()
    serializer_class = HoldingGunlerSerializer
    permission_classes = [gunler_permissions.HoldingGunlerPermissions]

    def update(self, request, *args, **kwargs):
        return gunler_utils.holding_gunler_update(self, request, *args, **kwargs)

class HoldingIstisnaIsciListCreateAPIView(generics.ListCreateAPIView):
    queryset = HoldingIstisnaIsci.objects.all()
    serializer_class = HoldingIstisnaIsciSerializer
    permission_classes = [gunler_permissions.HoldingIstisnaIsciPermissions]

    def create(self, request, *args, **kwargs):
        return gunler_utils.holding_istisna_isci_gunler_create(self, request, *args, **kwargs)

class HoldingIstisnaIsciDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HoldingIstisnaIsci.objects.all()
    serializer_class = HoldingIstisnaIsciSerializer
    permission_classes = [gunler_permissions.HoldingIstisnaIsciPermissions]

    def update(self, request, *args, **kwargs):
        return gunler_utils.holding_istisna_isci_gunler_update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return gunler_utils.holding_istisna_isci_gunler_delete(self, request, *args, **kwargs)

# ********************************** Shirket Gunler get post put delete **********************************
class ShirketGunlerListCreateAPIView(generics.ListAPIView):
    queryset = ShirketGunler.objects.all()
    serializer_class = ShirketGunlerSerializer
    permission_classes = [gunler_permissions.ShirketGunlerPermissions]


class ShirketGunlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShirketGunler.objects.all()
    serializer_class = ShirketGunlerSerializer
    permission_classes = [gunler_permissions.ShirketGunlerPermissions]

    def update(self, request, *args, **kwargs):
        return gunler_utils.shirket_gunler_update(self, request, *args, **kwargs)

class ShirketIstisnaIsciListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShirketIstisnaIsci.objects.all()
    serializer_class = ShirketIstisnaIsciSerializer
    permission_classes = [gunler_permissions.ShirketIstisnaIsciPermissions]

    def create(self, request, *args, **kwargs):
        return gunler_utils.shirket_istisna_isci_gunler_create(self, request, *args, **kwargs)

class ShirketIstisnaIsciDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShirketIstisnaIsci.objects.all()
    serializer_class = ShirketIstisnaIsciSerializer
    permission_classes = [gunler_permissions.ShirketIstisnaIsciPermissions]

    def update(self, request, *args, **kwargs):
        return gunler_utils.shirket_istisna_isci_gunler_update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return gunler_utils.shirket_istisna_isci_gunler_delete(self, request, *args, **kwargs)

# ********************************** Ofis Gunler get post put delete **********************************
class OfisGunlerListCreateAPIView(generics.ListAPIView):
    queryset = OfisGunler.objects.all()
    serializer_class = OfisGunlerSerializer
    permission_classes = [gunler_permissions.OfisGunlerPermissions]


class OfisGunlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfisGunler.objects.all()
    serializer_class = OfisGunlerSerializer
    permission_classes = [gunler_permissions.OfisGunlerPermissions]

    def update(self, request, *args, **kwargs):
        return gunler_utils.ofis_gunler_update(self, request, *args, **kwargs)

class OfisIstisnaIsciListCreateAPIView(generics.ListCreateAPIView):
    queryset = OfisIstisnaIsci.objects.all()
    serializer_class = OfisIstisnaIsciSerializer
    permission_classes = [gunler_permissions.OfisIstisnaIsciPermissions]

    def create(self, request, *args, **kwargs):
        return gunler_utils.ofis_istisna_isci_gunler_create(self, request, *args, **kwargs)

class OfisIstisnaIsciDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfisIstisnaIsci.objects.all()
    serializer_class = OfisIstisnaIsciSerializer
    permission_classes = [gunler_permissions.OfisIstisnaIsciPermissions]

    def update(self, request, *args, **kwargs):
        return gunler_utils.ofis_istisna_isci_gunler_update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return gunler_utils.ofis_istisna_isci_gunler_delete(self, request, *args, **kwargs)

# ********************************** Shobe Gunler get post put delete **********************************
class ShobeGunlerListCreateAPIView(generics.ListAPIView):
    queryset = ShobeGunler.objects.all()
    serializer_class = ShobeGunlerSerializer
    permission_classes = [gunler_permissions.ShobeGunlerPermissions]


class ShobeGunlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShobeGunler.objects.all()
    serializer_class = ShobeGunlerSerializer
    permission_classes = [gunler_permissions.ShobeGunlerPermissions]

    def update(self, request, *args, **kwargs):
        return gunler_utils.shobe_gunler_update(self, request, *args, **kwargs)

class ShobeIstisnaIsciListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShobeIstisnaIsci.objects.all()
    serializer_class = ShobeIstisnaIsciSerializer
    permission_classes = [gunler_permissions.ShobeIstisnaIsciPermissions]

    def create(self, request, *args, **kwargs):
        return gunler_utils.shobe_istisna_isci_gunler_create(self, request, *args, **kwargs)

class ShobeIstisnaIsciDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShobeIstisnaIsci.objects.all()
    serializer_class = ShobeIstisnaIsciSerializer
    permission_classes = [gunler_permissions.ShobeIstisnaIsciPermissions]

    def update(self, request, *args, **kwargs):
        return gunler_utils.shobe_istisna_isci_gunler_update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return gunler_utils.shobe_istisna_isci_gunler_delete(self, request, *args, **kwargs)

# ********************************** Komanda Gunler get post put delete **********************************
class KomandaGunlerListCreateAPIView(generics.ListAPIView):
    queryset = KomandaGunler.objects.all()
    serializer_class = KomandaGunlerSerializer
    permission_classes = [gunler_permissions.KomandaGunlerPermissions]


class KomandaGunlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KomandaGunler.objects.all()
    serializer_class = KomandaGunlerSerializer
    permission_classes = [gunler_permissions.KomandaGunlerPermissions]

    def update(self, request, *args, **kwargs):
        return gunler_utils.komanda_gunler_update(self, request, *args, **kwargs)

class KomandaIstisnaIsciListCreateAPIView(generics.ListCreateAPIView):
    queryset = KomandaIstisnaIsci.objects.all()
    serializer_class = KomandaIstisnaIsciSerializer
    permission_classes = [gunler_permissions.KomandaIstisnaIsciPermissions]

    def create(self, request, *args, **kwargs):
        return gunler_utils.komanda_istisna_isci_gunler_create(self, request, *args, **kwargs)

class KomandaIstisnaIsciDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KomandaIstisnaIsci.objects.all()
    serializer_class = KomandaIstisnaIsciSerializer
    permission_classes = [gunler_permissions.KomandaIstisnaIsciPermissions]

    def update(self, request, *args, **kwargs):
        return gunler_utils.komanda_istisna_isci_gunler_update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return gunler_utils.komanda_istisna_isci_gunler_delete(self, request, *args, **kwargs)

# ********************************** Vezife Gunler get post put delete **********************************
class VezifeGunlerListCreateAPIView(generics.ListAPIView):
    queryset = VezifeGunler.objects.all()
    serializer_class = VezifeGunlerSerializer
    permission_classes = [gunler_permissions.VezifeGunlerPermissions]

class VezifeGunlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VezifeGunler.objects.all()
    serializer_class = VezifeGunlerSerializer
    permission_classes = [gunler_permissions.VezifeGunlerPermissions]

    def update(self, request, *args, **kwargs):
        return gunler_utils.vezife_gunler_update(self, request, *args, **kwargs)

class VezifeIstisnaIsciListCreateAPIView(generics.ListCreateAPIView):
    queryset = VezifeIstisnaIsci.objects.all()
    serializer_class = VezifeIstisnaIsciSerializer
    permission_classes = [gunler_permissions.VezifeIstisnaIsciPermissions]

    def create(self, request, *args, **kwargs):
        return gunler_utils.vezife_istisna_isci_gunler_create(self, request, *args, **kwargs)

class VezifeIstisnaIsciDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VezifeIstisnaIsci.objects.all()
    serializer_class = VezifeIstisnaIsciSerializer
    permission_classes = [gunler_permissions.VezifeIstisnaIsciPermissions]

    def update(self, request, *args, **kwargs):
        return gunler_utils.vezife_istisna_isci_gunler_update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return gunler_utils.vezife_istisna_isci_gunler_delete(self, request, *args, **kwargs)
    
# ********************************** Isci Gunler get post put delete **********************************
class IsciGunlerListCreateAPIView(generics.ListAPIView):
    queryset = IsciGunler.objects.all()
    serializer_class = IsciGunlerSerializer
    permission_classes = [gunler_permissions.IsciGunlerPermissions]


class IsciGunlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IsciGunler.objects.all()
    serializer_class = IsciGunlerSerializer
    permission_classes = [gunler_permissions.IsciGunlerPermissions]

    def update(self, request, *args, **kwargs):
        return gunler_utils.user_gunler_update(self, request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return gunler_utils.user_gunler_patch(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return gunler_utils.user_gunler_delete(self, request, *args, **kwargs)

# ********************************** Isci Gelib getme vaxtlari get post put delete **********************************
class IsciGelibGetmeVaxtlariListCreateAPIView(generics.ListCreateAPIView):
    queryset = IsciGelibGetmeVaxtlari.objects.all()
    serializer_class = IsciGelibGetmeVaxtlariSerializer
    permission_classes = [gunler_permissions.IsciGelibGetmeVaxtlariPermissions]

class IsciGelibGetmeVaxtlariDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IsciGelibGetmeVaxtlari.objects.all()
    serializer_class = IsciGelibGetmeVaxtlariSerializer
    permission_classes = [gunler_permissions.IsciGelibGetmeVaxtlariPermissions]
