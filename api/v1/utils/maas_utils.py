from maas.models import Avans,Kesinti,MaasGoruntuleme
from api.v1.all_serializers.maas_serializers import AvansSerializer,KesintiSerializer,MaasGoruntulemeSerializer
from rest_framework import status, generics
from rest_framework.generics import get_object_or_404

from rest_framework.response import Response


# def prim_create(self, request, *args, **kwargs):
#     serializer = self.get_serializer(data=request.data)
#     if serializer.is_valid():
#         odenis_uslubu = serializer.validated_data.get("odenis_uslubu")
#         print(f"odenis_uslubu ==> {odenis_uslubu} -- {type(odenis_uslubu)}")

#         vezife = serializer.validated_data.get("vezife")
#         print(f"vezife ==> {vezife} -- {type(vezife)}")

#         mehsul = serializer.validated_data.get("mehsul")
#         print(f"mehsul ==> {mehsul} -- {type(mehsul)}")

#         prim_status = serializer.validated_data.get("prim_status")
#         print(f"prim_status ==> {prim_status} -- {type(prim_status)}")

#         komandaya_gore_bonus = serializer.validated_data.get("komandaya_gore_bonus")
#         print(f"komandaya_gore_bonus ==> {komandaya_gore_bonus} -- {type(komandaya_gore_bonus)}")

#         ofise_gore_bonus = serializer.validated_data.get("ofise_gore_bonus")
#         print(f"ofise_gore_bonus ==> {ofise_gore_bonus} -- {type(ofise_gore_bonus)}")

#         satis_meblegi = mehsul.qiymet
#         print(f"satis_meblegi ==> {satis_meblegi} -- {type(satis_meblegi)}")

#         serializer.save(satis_meblegi=satis_meblegi)

#         return Response({"detail": "Prim create olundu"}, status=status.HTTP_201_CREATED)