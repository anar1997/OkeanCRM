from rest_framework import status, generics
from rest_framework.generics import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend


from rest_framework.response import Response

from api.v1.all_serializers.company_serializers import (
    MuqavileKreditorSerializer,
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
    MuqavileKreditor,
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

from api.v1.filters.company_filters.filters import (
    HoldingKassaMedaxilFilter,
    HoldingKassaMexaricFilter,
    HoldingdenShirketlereTransferFilter,
    KomandaFilter,
    OfisFilter,
    OfisKassaFilter,
    OfisKassaMedaxilFilter,
    OfisKassaMexaricFilter,
    OfisdenShirketeTransferFilter,
    ShirketFilter,
    ShirketKassaFilter,
    ShirketKassaMedaxilFilter,
    ShirketKassaMexaricFilter,
    ShirketdenHoldingeTransferFilter,
    ShirketdenOfislereTransferFilter,
    ShobeFilter,
    VezifeFilter
)

from api.v1.permissions.company_permissions import permissions as company_permissions


# ********************************** komanda get post put delete **********************************


class KomandaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Komanda.objects.all()
    serializer_class = KomandaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = KomandaFilter
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
    filter_backends = [DjangoFilterBackend]
    filterset_class = KomandaFilter
    permission_classes = [company_permissions.KomandaPermissions]

    def destroy(self, request, *args, **kwargs):
        komanda = self.get_object()
        komanda.is_active = False
        komanda.save()
        return Response({"detail": "Komanda qeyri-atkiv edildi"}, status=status.HTTP_200_OK)



# ********************************** ofisler put delete post get **********************************


class OfisListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ofis.objects.all()
    serializer_class = OfisSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OfisFilter
    permission_classes = [company_permissions.OfisPermissions]



class OfisDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ofis.objects.all()
    serializer_class = OfisSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OfisFilter
    permission_classes = [company_permissions.OfisPermissions]



# ********************************** vezifeler put delete post get **********************************


class VezifelerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vezifeler.objects.all()
    serializer_class = VezifelerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = VezifeFilter
    permission_classes = [company_permissions.VezifelerPermissions]



class VezifelerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vezifeler.objects.all()
    serializer_class = VezifelerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = VezifeFilter
    permission_classes = [company_permissions.VezifelerPermissions]



# ********************************** shirket put delete post get **********************************
class ShirketListCreateAPIView(generics.ListCreateAPIView):
    queryset = Shirket.objects.all()
    serializer_class = ShirketSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShirketFilter
    permission_classes = [company_permissions.ShirketPermissions]



class ShirketDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shirket.objects.all()
    serializer_class = ShirketSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShirketFilter
    permission_classes = [company_permissions.ShirketPermissions]



# ********************************** shobe put delete post get **********************************


class ShobeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Shobe.objects.all()
    serializer_class = ShobeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShobeFilter
    permission_classes = [company_permissions.ShobePermissions]



class ShobeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shobe.objects.all()
    serializer_class = ShobeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShobeFilter
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
    filter_backends = [DjangoFilterBackend]
    filterset_class = HoldingKassaMedaxilFilter
    permission_classes = [company_permissions.HoldingKassaPermissions]



class HoldingKassaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HoldingKassa.objects.all()
    serializer_class = HoldingKassaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HoldingKassaMedaxilFilter
    permission_classes = [company_permissions.HoldingKassaPermissions]



# **********************************

class ShirketKassaListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShirketKassa.objects.all()
    serializer_class = ShirketKassaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShirketKassaFilter
    permission_classes = [company_permissions.ShirketKassaPermissions]



class ShirketKassaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShirketKassa.objects.all()
    serializer_class = ShirketKassaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShirketKassaFilter
    permission_classes = [company_permissions.ShirketKassaPermissions]



# **********************************

class OfisKassaListCreateAPIView(generics.ListCreateAPIView):
    queryset = OfisKassa.objects.all()
    serializer_class = OfisKassaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OfisKassaFilter
    permission_classes = [company_permissions.OfisKassaPermissions]



class OfisKassaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfisKassa.objects.all()
    serializer_class = OfisKassaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OfisKassaFilter
    permission_classes = [company_permissions.OfisKassaPermissions]



# ********************************** transfer put delete post get **********************************

class HoldingdenShirketlereTransferListCreateAPIView(generics.ListCreateAPIView):
    queryset = HoldingdenShirketlereTransfer.objects.all()
    serializer_class = HoldingdenShirketlereTransferSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HoldingdenShirketlereTransferFilter
    permission_classes = [company_permissions.HoldingdenShirketlereTransferPermissions]


    def create(self, request, *args, **kwargs):
        return kassa_transfer_utils.holding_shirket_transfer_create(self, request, *args, **kwargs)


class HoldingdenShirketlereTransferDetailAPIView(generics.RetrieveAPIView):
    queryset = HoldingdenShirketlereTransfer.objects.all()
    serializer_class = HoldingdenShirketlereTransferSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HoldingdenShirketlereTransferFilter
    permission_classes = [company_permissions.HoldingdenShirketlereTransferPermissions]



# **********************************

class ShirketdenHoldingeTransferListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShirketdenHoldingeTransfer.objects.all()
    serializer_class = ShirketdenHoldingeTransferSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShirketdenHoldingeTransferFilter
    permission_classes = [company_permissions.ShirketdenHoldingeTransferPermissions]


    def create(self, request, *args, **kwargs):
        return kassa_transfer_utils.shirket_holding_transfer_create(self, request, *args, **kwargs)


class ShirketdenHoldingeTransferDetailAPIView(generics.RetrieveAPIView):
    queryset = ShirketdenHoldingeTransfer.objects.all()
    serializer_class = ShirketdenHoldingeTransferSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShirketdenHoldingeTransferFilter
    permission_classes = [company_permissions.ShirketdenHoldingeTransferPermissions]



# **********************************

class OfisdenShirketeTransferListCreateAPIView(generics.ListCreateAPIView):
    queryset = OfisdenShirketeTransfer.objects.all()
    serializer_class = OfisdenShirketeTransferSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OfisdenShirketeTransferFilter
    permission_classes = [company_permissions.OfisdenShirketeTransferPermissions]


    def create(self, request, *args, **kwargs):
        return kassa_transfer_utils.ofis_shirket_transfer_create(self, request, *args, **kwargs)


class OfisdenShirketeTransferDetailAPIView(generics.RetrieveAPIView):
    queryset = OfisdenShirketeTransfer.objects.all()
    serializer_class = OfisdenShirketeTransferSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OfisdenShirketeTransferFilter
    permission_classes = [company_permissions.OfisdenShirketeTransferPermissions]



# **********************************

class ShirketdenOfislereTransferListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShirketdenOfislereTransfer.objects.all()
    serializer_class = ShirketdenOfislereTransferSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShirketdenOfislereTransferFilter
    permission_classes = [company_permissions.ShirketdenOfislereTransferPermissions]


    def create(self, request, *args, **kwargs):
        return kassa_transfer_utils.shirket_ofis_transfer_create(self, request, *args, **kwargs)


class ShirketdenOfislereTransferDetailAPIView(generics.RetrieveAPIView):
    queryset = ShirketdenOfislereTransfer.objects.all()
    serializer_class = ShirketdenOfislereTransferSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShirketdenOfislereTransferFilter
    permission_classes = [company_permissions.ShirketdenOfislereTransferPermissions]



# ********************************** holding kassa medaxil, mexaric put delete post get **********************************

class HoldingKassaMedaxilListCreateAPIView(generics.ListCreateAPIView):
    queryset = HoldingKassaMedaxil.objects.all()
    serializer_class = HoldingKassaMedaxilSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HoldingKassaMedaxilFilter
    permission_classes = [company_permissions.HoldingKassaMedaxilPermissions]


    def create(self, request, *args, **kwargs):
        return medaxil_mexaric_utils.holding_kassa_medaxil_create(self, request, *args, **kwargs)


class HoldingKassaMedaxilDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = HoldingKassaMedaxil.objects.all()
    serializer_class = HoldingKassaMedaxilSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HoldingKassaMedaxilFilter
    permission_classes = [company_permissions.HoldingKassaMedaxilPermissions]



# **********************************

class HoldingKassaMexaricListCreateAPIView(generics.ListCreateAPIView):
    queryset = HoldingKassaMexaric.objects.all()
    serializer_class = HoldingKassaMexaricSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HoldingKassaMexaricFilter
    permission_classes = [company_permissions.HoldingKassaMexaricPermissions]


    def create(self, request, *args, **kwargs):
        return medaxil_mexaric_utils.holding_kassa_mexaric_create(self, request, *args, **kwargs)


class HoldingKassaMexaricDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = HoldingKassaMexaric.objects.all()
    serializer_class = HoldingKassaMexaricSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HoldingKassaMexaricFilter
    permission_classes = [company_permissions.HoldingKassaMexaricPermissions]



# ********************************** shirket kassa medaxil, mexaric put delete post get **********************************

class ShirketKassaMedaxilListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShirketKassaMedaxil.objects.all()
    serializer_class = ShirketKassaMedaxilSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShirketKassaMedaxilFilter
    permission_classes = [company_permissions.ShirketKassaMedaxilPermissions]


    def create(self, request, *args, **kwargs):
        return medaxil_mexaric_utils.shirket_kassa_medaxil_create(self, request, *args, **kwargs)


class ShirketKassaMedaxilDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = ShirketKassaMedaxil.objects.all()
    serializer_class = ShirketKassaMedaxilSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShirketKassaMedaxilFilter
    permission_classes = [company_permissions.ShirketKassaMedaxilPermissions]



# **********************************

class ShirketKassaMexaricListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShirketKassaMexaric.objects.all()
    serializer_class = ShirketKassaMexaricSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShirketKassaMexaricFilter
    permission_classes = [company_permissions.ShirketKassaMexaricPermissions]


    def create(self, request, *args, **kwargs):
        return medaxil_mexaric_utils.shirket_kassa_mexaric_create(self, request, *args, **kwargs)


class ShirketKassaMexaricDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = ShirketKassaMexaric.objects.all()
    serializer_class = ShirketKassaMexaricSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShirketKassaMexaricFilter
    permission_classes = [company_permissions.ShirketKassaMexaricPermissions]



# ********************************** Ofis kassa medaxil, mexaric put delete post get **********************************

class OfisKassaMedaxilListCreateAPIView(generics.ListCreateAPIView):
    queryset = OfisKassaMedaxil.objects.all()
    serializer_class = OfisKassaMedaxilSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OfisKassaMedaxilFilter
    permission_classes = [company_permissions.OfisKassaMedaxilPermissions]


    def create(self, request, *args, **kwargs):
        return medaxil_mexaric_utils.ofis_kassa_medaxil_create(self, request, *args, **kwargs)


class OfisKassaMedaxilDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = OfisKassaMedaxil.objects.all()
    serializer_class = OfisKassaMedaxilSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OfisKassaMedaxilFilter
    permission_classes = [company_permissions.OfisKassaMedaxilPermissions]



# **********************************

class OfisKassaMexaricListCreateAPIView(generics.ListCreateAPIView):
    queryset = OfisKassaMexaric.objects.all()
    serializer_class = OfisKassaMexaricSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OfisKassaMexaricFilter
    permission_classes = [company_permissions.OfisKassaMexaricPermissions]


    def create(self, request, *args, **kwargs):
        return medaxil_mexaric_utils.ofis_kassa_mexaric_create(self, request, *args, **kwargs)


class OfisKassaMexaricDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = OfisKassaMexaric.objects.all()
    serializer_class = OfisKassaMexaricSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OfisKassaMexaricFilter
    permission_classes = [company_permissions.OfisKassaMexaricPermissions]

# **********************************

class MuqavileKreditorListCreateAPIView(generics.ListCreateAPIView):
    queryset = MuqavileKreditor.objects.all()
    serializer_class = MuqavileKreditorSerializer
    permission_classes = [company_permissions.MuqavileKreditorPermissions]

class MuqavileKreditorDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = MuqavileKreditor.objects.all()
    serializer_class = MuqavileKreditorSerializer
    permission_classes = [company_permissions.MuqavileKreditorPermissions]
