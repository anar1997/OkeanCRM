from rest_framework import status, generics
from rest_framework.generics import get_object_or_404

from rest_framework.response import Response

from api.v1.all_serializers.company_serializers import (
    OfisKassaMedaxilSerializer,
    OfisKassaMexaricSerializer,
    ShirketKassaMedaxilSerializer,
    ShirketKassaMexaricSerializer,
    ShirketSerializer,
    KomandaSerializer,
    OfisSerializer,
    ShobeSerializer,
    VezifelerSerializer,
    HoldingSerializer,
    HoldingKassaSerializer,
    ShirketKassaSerializer,
    OfisKassaSerializer,
    HoldingdenShirketlereTransferSerializer,
    ShirketdenHoldingeTransferSerializer,
    OfisdenShirketeTransferSerializer,
    ShirketdenOfislereTransferSerializer,
    HoldingKassaMedaxilSerializer,
    HoldingKassaMexaricSerializer
)

from account.models import User

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

from api.v1.utils import (
    medaxil_mexaric_utils,
    kassa_transfer_utils
)

from api.v1.permissions.company_permissions import permissions as company_permissions


# ********************************** komanda get post put delete **********************************


class KomandaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Komanda.objects.all()
    serializer_class = KomandaSerializer
    permission_classes = [company_permissions.KomandaPermissions]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"detail": "Komanda müvəffəqiyyətlə düzəldildi"}, status=status.HTTP_201_CREATED,
                        headers=headers)


class KomandaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Komanda.objects.all()
    serializer_class = KomandaSerializer
    permission_classes = [company_permissions.KomandaPermissions]



# ********************************** ofisler put delete post get **********************************


class OfisListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ofis.objects.all()
    serializer_class = OfisSerializer
    permission_classes = [company_permissions.OfisPermissions]



class OfisDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ofis.objects.all()
    serializer_class = OfisSerializer
    permission_classes = [company_permissions.OfisPermissions]



# ********************************** vezifeler put delete post get **********************************


class VezifelerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vezifeler.objects.all()
    serializer_class = VezifelerSerializer
    permission_classes = [company_permissions.VezifelerPermissions]



class VezifelerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vezifeler.objects.all()
    serializer_class = VezifelerSerializer
    permission_classes = [company_permissions.VezifelerPermissions]



# ********************************** shirket put delete post get **********************************
class ShirketListCreateAPIView(generics.ListCreateAPIView):
    queryset = Shirket.objects.all()
    serializer_class = ShirketSerializer
    permission_classes = [company_permissions.ShirketPermissions]



class ShirketDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shirket.objects.all()
    serializer_class = ShirketSerializer
    permission_classes = [company_permissions.ShirketPermissions]



# ********************************** shobe put delete post get **********************************


class ShobeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Shobe.objects.all()
    serializer_class = ShobeSerializer
    permission_classes = [company_permissions.ShobePermissions]



class ShobeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shobe.objects.all()
    serializer_class = ShobeSerializer
    permission_classes = [company_permissions.ShobePermissions]



# ********************************** holding put delete post get **********************************

class HoldingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Holding.objects.all()
    serializer_class = HoldingSerializer
    permission_classes = [company_permissions.HoldingPermissions]



class HoldingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Holding.objects.all()
    serializer_class = HoldingSerializer
    permission_classes = [company_permissions.HoldingPermissions]



# ********************************** kassa put delete post get **********************************

class HoldingKassaListCreateAPIView(generics.ListCreateAPIView):
    queryset = HoldingKassa.objects.all()
    serializer_class = HoldingKassaSerializer
    permission_classes = [company_permissions.HoldingKassaPermissions]



class HoldingKassaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HoldingKassa.objects.all()
    serializer_class = HoldingKassaSerializer
    permission_classes = [company_permissions.HoldingKassaPermissions]



# **********************************

class ShirketKassaListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShirketKassa.objects.all()
    serializer_class = ShirketKassaSerializer
    permission_classes = [company_permissions.ShirketKassaPermissions]



class ShirketKassaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShirketKassa.objects.all()
    serializer_class = ShirketKassaSerializer
    permission_classes = [company_permissions.ShirketKassaPermissions]



# **********************************

class OfisKassaListCreateAPIView(generics.ListCreateAPIView):
    queryset = OfisKassa.objects.all()
    serializer_class = OfisKassaSerializer
    permission_classes = [company_permissions.OfisKassaPermissions]



class OfisKassaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfisKassa.objects.all()
    serializer_class = OfisKassaSerializer
    permission_classes = [company_permissions.OfisKassaPermissions]



# ********************************** transfer put delete post get **********************************

class HoldingdenShirketlereTransferListCreateAPIView(generics.ListCreateAPIView):
    queryset = HoldingdenShirketlereTransfer.objects.all()
    serializer_class = HoldingdenShirketlereTransferSerializer
    permission_classes = [company_permissions.HoldingdenShirketlereTransferPermissions]


    def create(self, request, *args, **kwargs):
        return kassa_transfer_utils.holding_shirket_transfer_create(self, request, *args, **kwargs)


class HoldingdenShirketlereTransferDetailAPIView(generics.RetrieveAPIView):
    queryset = HoldingdenShirketlereTransfer.objects.all()
    serializer_class = HoldingdenShirketlereTransferSerializer
    permission_classes = [company_permissions.HoldingdenShirketlereTransferPermissions]



# **********************************

class ShirketdenHoldingeTransferListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShirketdenHoldingeTransfer.objects.all()
    serializer_class = ShirketdenHoldingeTransferSerializer
    permission_classes = [company_permissions.ShirketdenHoldingeTransferPermissions]


    def create(self, request, *args, **kwargs):
        return kassa_transfer_utils.shirket_holding_transfer_create(self, request, *args, **kwargs)


class ShirketdenHoldingeTransferDetailAPIView(generics.RetrieveAPIView):
    queryset = ShirketdenHoldingeTransfer.objects.all()
    serializer_class = ShirketdenHoldingeTransferSerializer
    permission_classes = [company_permissions.ShirketdenHoldingeTransferPermissions]



# **********************************

class OfisdenShirketeTransferListCreateAPIView(generics.ListCreateAPIView):
    queryset = OfisdenShirketeTransfer.objects.all()
    serializer_class = OfisdenShirketeTransferSerializer
    permission_classes = [company_permissions.OfisdenShirketeTransferPermissions]


    def create(self, request, *args, **kwargs):
        return kassa_transfer_utils.ofis_shirket_transfer_create(self, request, *args, **kwargs)


class OfisdenShirketeTransferDetailAPIView(generics.RetrieveAPIView):
    queryset = OfisdenShirketeTransfer.objects.all()
    serializer_class = OfisdenShirketeTransferSerializer
    permission_classes = [company_permissions.OfisdenShirketeTransferPermissions]



# **********************************

class ShirketdenOfislereTransferListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShirketdenOfislereTransfer.objects.all()
    serializer_class = ShirketdenOfislereTransferSerializer
    permission_classes = [company_permissions.ShirketdenOfislereTransferPermissions]


    def create(self, request, *args, **kwargs):
        return kassa_transfer_utils.shirket_ofis_transfer_create(self, request, *args, **kwargs)


class ShirketdenOfislereTransferDetailAPIView(generics.RetrieveAPIView):
    queryset = ShirketdenOfislereTransfer.objects.all()
    serializer_class = ShirketdenOfislereTransferSerializer
    permission_classes = [company_permissions.ShirketdenOfislereTransferPermissions]



# ********************************** holding kassa medaxil, mexaric put delete post get **********************************

class HoldingKassaMedaxilListCreateAPIView(generics.ListCreateAPIView):
    queryset = HoldingKassaMedaxil.objects.all()
    serializer_class = HoldingKassaMedaxilSerializer
    permission_classes = [company_permissions.HoldingKassaMedaxilPermissions]


    def create(self, request, *args, **kwargs):
        return medaxil_mexaric_utils.holding_kassa_medaxil_create(self, request, *args, **kwargs)


class HoldingKassaMedaxilDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HoldingKassaMedaxil.objects.all()
    serializer_class = HoldingKassaMedaxilSerializer
    permission_classes = [company_permissions.HoldingKassaMedaxilPermissions]



# **********************************

class HoldingKassaMexaricListCreateAPIView(generics.ListCreateAPIView):
    queryset = HoldingKassaMexaric.objects.all()
    serializer_class = HoldingKassaMexaricSerializer
    permission_classes = [company_permissions.HoldingKassaMexaricPermissions]


    def create(self, request, *args, **kwargs):
        return medaxil_mexaric_utils.holding_kassa_mexaric_create(self, request, *args, **kwargs)


class HoldingKassaMexaricDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HoldingKassaMexaric.objects.all()
    serializer_class = HoldingKassaMexaricSerializer
    permission_classes = [company_permissions.HoldingKassaMexaricPermissions]



# ********************************** shirket kassa medaxil, mexaric put delete post get **********************************

class ShirketKassaMedaxilListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShirketKassaMedaxil.objects.all()
    serializer_class = ShirketKassaMedaxilSerializer
    permission_classes = [company_permissions.ShirketKassaMedaxilPermissions]


    def create(self, request, *args, **kwargs):
        return medaxil_mexaric_utils.shirket_kassa_medaxil_create(self, request, *args, **kwargs)


class ShirketKassaMedaxilDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShirketKassaMedaxil.objects.all()
    serializer_class = ShirketKassaMedaxilSerializer
    permission_classes = [company_permissions.ShirketKassaMedaxilPermissions]



# **********************************

class ShirketKassaMexaricListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShirketKassaMexaric.objects.all()
    serializer_class = ShirketKassaMexaricSerializer
    permission_classes = [company_permissions.ShirketKassaMexaricPermissions]


    def create(self, request, *args, **kwargs):
        return medaxil_mexaric_utils.shirket_kassa_mexaric_create(self, request, *args, **kwargs)


class ShirketKassaMexaricDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShirketKassaMexaric.objects.all()
    serializer_class = ShirketKassaMexaricSerializer
    permission_classes = [company_permissions.ShirketKassaMexaricPermissions]



# ********************************** Ofis kassa medaxil, mexaric put delete post get **********************************

class OfisKassaMedaxilListCreateAPIView(generics.ListCreateAPIView):
    queryset = OfisKassaMedaxil.objects.all()
    serializer_class = OfisKassaMedaxilSerializer
    permission_classes = [company_permissions.OfisKassaMedaxilPermissions]


    def create(self, request, *args, **kwargs):
        return medaxil_mexaric_utils.ofis_kassa_medaxil_create(self, request, *args, **kwargs)


class OfisKassaMedaxilDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfisKassaMedaxil.objects.all()
    serializer_class = OfisKassaMedaxilSerializer
    permission_classes = [company_permissions.OfisKassaMedaxilPermissions]



# **********************************

class OfisKassaMexaricListCreateAPIView(generics.ListCreateAPIView):
    queryset = OfisKassaMexaric.objects.all()
    serializer_class = OfisKassaMexaricSerializer
    permission_classes = [company_permissions.OfisKassaMexaricPermissions]


    def create(self, request, *args, **kwargs):
        return medaxil_mexaric_utils.ofis_kassa_mexaric_create(self, request, *args, **kwargs)


class OfisKassaMexaricDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfisKassaMexaric.objects.all()
    serializer_class = OfisKassaMexaricSerializer
    permission_classes = [company_permissions.OfisKassaMexaricPermissions]

