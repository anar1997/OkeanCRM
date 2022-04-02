from maas.models import (
    Avans,
    Kesinti,
    Bonus,
    MaasGoruntuleme, 
    VanLeaderPrim, 
    DealerPrim, 
    OfficeLeaderPrim,
    CanvasserPrim
)
from api.v1.all_serializers.maas_serializers import (
    AvansSerializer, 
    BonusSerializer,
    KesintiSerializer,
    MaasGoruntulemeSerializer,
    CanvasserPrimSerializer,
    DealerPrimSerializer,
    OfficeLeaderPrimSerializer,
    VanLeaderPrimSerializer,
)
from rest_framework import status, generics
from rest_framework.generics import get_object_or_404

from rest_framework.response import Response

from api.v1.utils import (
    maas_utils
)

# ********************************** Avans get post put delete **********************************
class AvansListCreateAPIView(generics.ListCreateAPIView):
    queryset = Avans.objects.all()
    serializer_class = AvansSerializer


class AvansDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avans.objects.all()
    serializer_class = AvansSerializer

# ********************************** Kesinti get post put delete **********************************
class KesintiListCreateAPIView(generics.ListCreateAPIView):
    queryset = Kesinti.objects.all()
    serializer_class = KesintiSerializer


class KesintiDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kesinti.objects.all()
    serializer_class = KesintiSerializer

# ********************************** MaasGoruntuleme get post put delete **********************************
class MaasGoruntulemeListCreateAPIView(generics.ListCreateAPIView):
    queryset = MaasGoruntuleme.objects.all()
    serializer_class = MaasGoruntulemeSerializer


class MaasGoruntulemeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaasGoruntuleme.objects.all()
    serializer_class = MaasGoruntulemeSerializer

# ********************************** Bonus get post put delete **********************************
class BonusListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer

    def create(self, request, *args, **kwargs):
        return maas_utils.bonus_create(self, request, *args, **kwargs)


class BonusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer

# ********************************** Office Leader Prim get post put delete **********************************
class OfficeLeaderPrimListCreateAPIView(generics.ListCreateAPIView):
    queryset = OfficeLeaderPrim.objects.all()
    serializer_class = OfficeLeaderPrimSerializer


class OfficeLeaderPrimDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfficeLeaderPrim.objects.all()
    serializer_class = OfficeLeaderPrimSerializer

# ********************************** VanLeader Prim get post put delete **********************************
class VanLeaderPrimListCreateAPIView(generics.ListCreateAPIView):
    queryset = VanLeaderPrim.objects.all()
    serializer_class = VanLeaderPrimSerializer


class VanLeaderPrimDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VanLeaderPrim.objects.all()
    serializer_class = VanLeaderPrimSerializer

# ********************************** Canvasser Prim get post put delete **********************************
class CanvasserPrimListCreateAPIView(generics.ListCreateAPIView):
    queryset = CanvasserPrim.objects.all()
    serializer_class = CanvasserPrimSerializer


class CanvasserPrimDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CanvasserPrim.objects.all()
    serializer_class = CanvasserPrimSerializer

# ********************************** Dealer Prim get post put delete **********************************
class DealerPrimListCreateAPIView(generics.ListCreateAPIView):
    queryset = DealerPrim.objects.all()
    serializer_class = DealerPrimSerializer


class DealerPrimDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DealerPrim.objects.all()
    serializer_class = DealerPrimSerializer