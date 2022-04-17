from maas.models import (
    Avans,
    Kesinti,
    Bonus,
    MaasGoruntuleme,
    MaasOde, 
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
    MaasOdeSerializer,
    OfficeLeaderPrimSerializer,
    VanLeaderPrimSerializer,
)
from rest_framework import status, generics
from rest_framework.generics import get_object_or_404

from rest_framework.response import Response

from api.v1.utils import (
    maas_utils
)

from api.v1.permissions.maas_permissions import permissions as maas_permissions

# ********************************** Avans get post put delete **********************************
class AvansListCreateAPIView(generics.ListCreateAPIView):
    queryset = Avans.objects.all()
    serializer_class = AvansSerializer
    permission_classes = [maas_permissions.AvansPermissions]

    def create(self, request, *args, **kwargs):
        return maas_utils.avans_create(self, request, *args, **kwargs)

class AvansDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Avans.objects.all()
    serializer_class = AvansSerializer
    permission_classes = [maas_permissions.AvansPermissions]

# ********************************** Kesinti get post put delete **********************************
class KesintiListCreateAPIView(generics.ListCreateAPIView):
    queryset = Kesinti.objects.all()
    serializer_class = KesintiSerializer
    permission_classes = [maas_permissions.KesintiPermissions]

    def create(self, request, *args, **kwargs):
        return maas_utils.kesinti_create(self, request, *args, **kwargs)


class KesintiDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Kesinti.objects.all()
    serializer_class = KesintiSerializer
    permission_classes = [maas_permissions.KesintiPermissions]

# ********************************** Bonus get post put delete **********************************
class BonusListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer
    permission_classes = [maas_permissions.BonusPermissions]

    def create(self, request, *args, **kwargs):
        return maas_utils.bonus_create(self, request, *args, **kwargs)


class BonusDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer
    permission_classes = [maas_permissions.BonusPermissions]

# ********************************** Maas Ode get post put delete **********************************
class MaasOdeListCreateAPIView(generics.ListCreateAPIView):
    queryset = MaasOde.objects.all()
    serializer_class = MaasOdeSerializer
    permission_classes = [maas_permissions.MaasOdePermissions]

    def create(self, request, *args, **kwargs):
        return maas_utils.maas_ode_create(self, request, *args, **kwargs)


class MaasOdeDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = MaasOde.objects.all()
    serializer_class = MaasOdeSerializer
    permission_classes = [maas_permissions.MaasOdePermissions]

# ********************************** MaasGoruntuleme get post put delete **********************************
class MaasGoruntulemeListCreateAPIView(generics.ListCreateAPIView):
    queryset = MaasGoruntuleme.objects.all()
    serializer_class = MaasGoruntulemeSerializer
    permission_classes = [maas_permissions.MaasGoruntulemePermissions]


class MaasGoruntulemeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaasGoruntuleme.objects.all()
    serializer_class = MaasGoruntulemeSerializer
    permission_classes = [maas_permissions.MaasGoruntulemePermissions]

# ********************************** Office Leader Prim get post put delete **********************************
class OfficeLeaderPrimListCreateAPIView(generics.ListCreateAPIView):
    queryset = OfficeLeaderPrim.objects.all()
    serializer_class = OfficeLeaderPrimSerializer
    permission_classes = [maas_permissions.OfficeLeaderPrimPermissions]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            mehsul = serializer.validated_data.get("mehsul")
            print(f"{mehsul=}")
            
            satis_meblegi = serializer.validated_data.get("satis_meblegi")
            print(f"{satis_meblegi=}")

            if (satis_meblegi == None) or (satis_meblegi == ""):
                satis_meblegi = mehsul.qiymet
            
            serializer.save(satis_meblegi=satis_meblegi)

            return Response({"detail": "Prim əlavə edildi"})


class OfficeLeaderPrimDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfficeLeaderPrim.objects.all()
    serializer_class = OfficeLeaderPrimSerializer
    permission_classes = [maas_permissions.OfficeLeaderPrimPermissions]

# ********************************** VanLeader Prim get post put delete **********************************
class VanLeaderPrimListCreateAPIView(generics.ListCreateAPIView):
    queryset = VanLeaderPrim.objects.all()
    serializer_class = VanLeaderPrimSerializer
    permission_classes = [maas_permissions.VanLeaderPrimPermissions]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            mehsul = serializer.validated_data.get("mehsul")
            print(f"{mehsul=}")
            
            satis_meblegi = serializer.validated_data.get("satis_meblegi")
            print(f"{satis_meblegi=}")

            if (satis_meblegi == None) or (satis_meblegi == ""):
                satis_meblegi = mehsul.qiymet
            
            serializer.save(satis_meblegi=satis_meblegi)

            return Response({"detail": "Prim əlavə edildi"})


class VanLeaderPrimDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VanLeaderPrim.objects.all()
    serializer_class = VanLeaderPrimSerializer
    permission_classes = [maas_permissions.VanLeaderPrimPermissions]

# ********************************** Canvasser Prim get post put delete **********************************
class CanvasserPrimListCreateAPIView(generics.ListCreateAPIView):
    queryset = CanvasserPrim.objects.all()
    serializer_class = CanvasserPrimSerializer
    permission_classes = [maas_permissions.CanvasserPrimPermissions]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            mehsul = serializer.validated_data.get("mehsul")
            print(f"{mehsul=}")
            
            satis_meblegi = serializer.validated_data.get("satis_meblegi")
            print(f"{satis_meblegi=}")

            if (satis_meblegi == None) or (satis_meblegi == ""):
                satis_meblegi = mehsul.qiymet
            
            serializer.save(satis_meblegi=satis_meblegi)

            return Response({"detail": "Prim əlavə edildi"})

class CanvasserPrimDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CanvasserPrim.objects.all()
    serializer_class = CanvasserPrimSerializer
    permission_classes = [maas_permissions.CanvasserPrimPermissions]

# ********************************** Dealer Prim get post put delete **********************************
class DealerPrimListCreateAPIView(generics.ListCreateAPIView):
    queryset = DealerPrim.objects.all()
    serializer_class = DealerPrimSerializer
    permission_classes = [maas_permissions.DealerPrimPermissions]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            mehsul = serializer.validated_data.get("mehsul")
            print(f"{mehsul=}")
            
            satis_meblegi = serializer.validated_data.get("satis_meblegi")
            print(f"{satis_meblegi=}")

            if (satis_meblegi == None) or (satis_meblegi == ""):
                satis_meblegi = mehsul.qiymet
            
            serializer.save(satis_meblegi=satis_meblegi)

            return Response({"detail": "Prim əlavə edildi"})

class DealerPrimDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DealerPrim.objects.all()
    serializer_class = DealerPrimSerializer
    permission_classes = [maas_permissions.DealerPrimPermissions]