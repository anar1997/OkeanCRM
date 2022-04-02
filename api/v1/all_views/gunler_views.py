from api.v1.all_serializers.gunler_serializers import (
    HoldingGunlerSerializer, 
    IsciGunlerSerializer, 
    KomandaGunlerSerializer, 
    OfisGunlerSerializer, 
    ShirketGunlerSerializer, 
    ShobeGunlerSerializer, 
    VezifeGunlerSerializer,
    HoldingIstisnaIsciSerializer
)
from gunler.models import (
    HoldingGunler,
    IsciGunler,
    KomandaGunler,
    OfisGunler,
    ShirketGunler,
    ShobeGunler,
    VezifeGunler,
    HoldingIstisnaIsci
)

from api.v1.utils import gunler_utils

from rest_framework import status, generics
from rest_framework.generics import get_object_or_404

from rest_framework.response import Response

# ********************************** Holding Gunler get post put delete **********************************
class HoldingGunlerListCreateAPIView(generics.ListCreateAPIView):
    queryset = HoldingGunler.objects.all()
    serializer_class = HoldingGunlerSerializer

class HoldingGunlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HoldingGunler.objects.all()
    serializer_class = HoldingGunlerSerializer

    def update(self, request, *args, **kwargs):
        return gunler_utils.holding_gunler_update(self, request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return gunler_utils.holding_gunler_patch(self, request, *args, **kwargs)

class HoldingIstisnaIsciListCreateAPIView(generics.ListCreateAPIView):
    queryset = HoldingIstisnaIsci.objects.all()
    serializer_class = HoldingIstisnaIsciSerializer

class HoldingIstisnaIsciDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HoldingIstisnaIsci.objects.all()
    serializer_class = HoldingIstisnaIsciSerializer

# ********************************** Shirket Gunler get post put delete **********************************
class ShirketGunlerListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShirketGunler.objects.all()
    serializer_class = ShirketGunlerSerializer


class ShirketGunlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShirketGunler.objects.all()
    serializer_class = ShirketGunlerSerializer

    def update(self, request, *args, **kwargs):
        return gunler_utils.shirket_gunler_update(self, request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return gunler_utils.shirket_gunler_patch(self, request, *args, **kwargs)

# ********************************** Ofis Gunler get post put delete **********************************
class OfisGunlerListCreateAPIView(generics.ListCreateAPIView):
    queryset = OfisGunler.objects.all()
    serializer_class = OfisGunlerSerializer


class OfisGunlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfisGunler.objects.all()
    serializer_class = OfisGunlerSerializer

    def update(self, request, *args, **kwargs):
        return gunler_utils.ofis_gunler_update(self, request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return gunler_utils.ofis_gunler_patch(self, request, *args, **kwargs)

# ********************************** Shobe Gunler get post put delete **********************************
class ShobeGunlerListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShobeGunler.objects.all()
    serializer_class = ShobeGunlerSerializer


class ShobeGunlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShobeGunler.objects.all()
    serializer_class = ShobeGunlerSerializer

    def update(self, request, *args, **kwargs):
        return gunler_utils.shobe_gunler_update(self, request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return gunler_utils.shobe_gunler_patch(self, request, *args, **kwargs)

# ********************************** Komanda Gunler get post put delete **********************************
class KomandaGunlerListCreateAPIView(generics.ListCreateAPIView):
    queryset = KomandaGunler.objects.all()
    serializer_class = KomandaGunlerSerializer


class KomandaGunlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KomandaGunler.objects.all()
    serializer_class = KomandaGunlerSerializer

    def update(self, request, *args, **kwargs):
        return gunler_utils.komanda_gunler_update(self, request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return gunler_utils.komanda_gunler_patch(self, request, *args, **kwargs)

# ********************************** Vezife Gunler get post put delete **********************************
class VezifeGunlerListCreateAPIView(generics.ListCreateAPIView):
    queryset = VezifeGunler.objects.all()
    serializer_class = VezifeGunlerSerializer


class VezifeGunlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VezifeGunler.objects.all()
    serializer_class = VezifeGunlerSerializer

    def update(self, request, *args, **kwargs):
        return gunler_utils.vezife_gunler_update(self, request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return gunler_utils.vezife_gunler_patch(self, request, *args, **kwargs)

# ********************************** Isci Gunler get post put delete **********************************
class IsciGunlerListCreateAPIView(generics.ListCreateAPIView):
    queryset = IsciGunler.objects.all()
    serializer_class = IsciGunlerSerializer


class IsciGunlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IsciGunler.objects.all()
    serializer_class = IsciGunlerSerializer

    def update(self, request, *args, **kwargs):
        return gunler_utils.user_gunler_update(self, request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return gunler_utils.user_gunler_patch(self, request, *args, **kwargs)