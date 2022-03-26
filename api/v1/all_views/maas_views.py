from maas.models import Avans,Kesinti,MaasGoruntuleme
from api.v1.all_serializers.maas_serializers import AvansSerializer,KesintiSerializer,MaasGoruntulemeSerializer
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

# ********************************** Prim get post put delete **********************************
# class PrimListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Prim.objects.all()
#     serializer_class = PrimSerializer

#     def create(self, request, *args, **kwargs):
#         return maas_utils.prim_create(self, request, *args, **kwargs)


# class PrimDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Prim.objects.all()
#     serializer_class = PrimSerializer
