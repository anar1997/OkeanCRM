from rest_framework import status, generics

from rest_framework.response import Response
from rest_framework import generics

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
)

# ********************************** komanda get post put delete **********************************


class KomandaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Komanda.objects.all()
    serializer_class = KomandaSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"detail": "Komanda müvəffəqiyyətlə düzəldildi"}, status=status.HTTP_201_CREATED, headers=headers)


class KomandaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Komanda.objects.all()
    serializer_class = KomandaSerializer

# ********************************** ofisler put delete post get **********************************


class OfisListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ofis.objects.all()
    serializer_class = OfisSerializer


class OfisDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ofis.objects.all()
    serializer_class = OfisSerializer


# ********************************** vezifeler put delete post get **********************************


class VezifelerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vezifeler.objects.all()
    serializer_class = VezifelerSerializer


class VezifelerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vezifeler.objects.all()
    serializer_class = VezifelerSerializer

# ********************************** shirket put delete post get **********************************
class ShirketListCreateAPIView(generics.ListCreateAPIView):
    queryset = Shirket.objects.all()
    serializer_class = ShirketSerializer


class ShirketDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shirket.objects.all()
    serializer_class = ShirketSerializer


# ********************************** shobe put delete post get **********************************


class ShobeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Shobe.objects.all()
    serializer_class = ShobeSerializer


class ShobeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shobe.objects.all()
    serializer_class = ShobeSerializer

# ********************************** holding put delete post get **********************************

class HoldingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Holding.objects.all()
    serializer_class = HoldingSerializer


class HoldingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Holding.objects.all()
    serializer_class = HoldingSerializer

# ********************************** kassa put delete post get **********************************

class HoldingKassaListCreateAPIView(generics.ListCreateAPIView):
    queryset = HoldingKassa.objects.all()
    serializer_class = HoldingKassaSerializer


class HoldingKassaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HoldingKassa.objects.all()
    serializer_class = HoldingKassaSerializer

# **********************************

class ShirketKassaListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShirketKassa.objects.all()
    serializer_class = ShirketKassaSerializer


class ShirketKassaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShirketKassa.objects.all()
    serializer_class = ShirketKassaSerializer

# **********************************

class OfisKassaListCreateAPIView(generics.ListCreateAPIView):
    queryset = OfisKassa.objects.all()
    serializer_class = OfisKassaSerializer


class OfisKassaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfisKassa.objects.all()
    serializer_class = OfisKassaSerializer

# ********************************** transfer put delete post get **********************************

class HoldingdenShirketlereTransferListCreateAPIView(generics.ListCreateAPIView):
    queryset = HoldingdenShirketlereTransfer.objects.all()
    serializer_class = HoldingdenShirketlereTransferSerializer


class HoldingdenShirketlereTransferDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HoldingdenShirketlereTransfer.objects.all()
    serializer_class = HoldingdenShirketlereTransferSerializer

# **********************************

class ShirketdenHoldingeTransferListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShirketdenHoldingeTransfer.objects.all()
    serializer_class = ShirketdenHoldingeTransferSerializer


class ShirketdenHoldingeTransferDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShirketdenHoldingeTransfer.objects.all()
    serializer_class = ShirketdenHoldingeTransferSerializer

# **********************************

class OfisdenShirketeTransferListCreateAPIView(generics.ListCreateAPIView):
    queryset = OfisdenShirketeTransfer.objects.all()
    serializer_class = OfisdenShirketeTransferSerializer


class OfisdenShirketeTransferDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfisdenShirketeTransfer.objects.all()
    serializer_class = OfisdenShirketeTransferSerializer

# **********************************

class ShirketdenOfislereTransferListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShirketdenOfislereTransfer.objects.all()
    serializer_class = ShirketdenOfislereTransferSerializer


class ShirketdenOfislereTransferDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShirketdenOfislereTransfer.objects.all()
    serializer_class = ShirketdenOfislereTransferSerializer


# ********************************** holding kassa medaxil, mexaric put delete post get **********************************

class HoldingKassaMedaxilListCreateAPIView(generics.ListCreateAPIView):
    queryset = HoldingKassaMedaxil.objects.all()
    serializer_class = HoldingKassaMedaxilSerializer

    def create(self, request, *args, **kwargs):
        return medaxil_mexaric_utils.holding_kassa_medaxil_create(self, request, *args, **kwargs)


class HoldingKassaMedaxilDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HoldingKassaMedaxil.objects.all()
    serializer_class = HoldingKassaMedaxilSerializer

# **********************************

class HoldingKassaMexaricListCreateAPIView(generics.ListCreateAPIView):
    queryset = HoldingKassaMexaric.objects.all()
    serializer_class = HoldingKassaMexaricSerializer

    def create(self, request, *args, **kwargs):
        return medaxil_mexaric_utils.holding_kassa_mexaric_create(self, request, *args, **kwargs)


class HoldingKassaMexaricDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HoldingKassaMexaric.objects.all()
    serializer_class = HoldingKassaMexaricSerializer

# ********************************** shirket kassa medaxil, mexaric put delete post get **********************************

class ShirketKassaMedaxilListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShirketKassaMedaxil.objects.all()
    serializer_class = ShirketKassaMedaxilSerializer

    def create(self, request, *args, **kwargs):
        return medaxil_mexaric_utils.shirket_kassa_medaxil_create(self, request, *args, **kwargs)


class ShirketKassaMedaxilDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShirketKassaMedaxil.objects.all()
    serializer_class = ShirketKassaMedaxilSerializer

# **********************************

class ShirketKassaMexaricListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShirketKassaMexaric.objects.all()
    serializer_class = ShirketKassaMexaricSerializer

    def create(self, request, *args, **kwargs):
        return medaxil_mexaric_utils.shirket_kassa_mexaric_create(self, request, *args, **kwargs)


class ShirketKassaMexaricDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShirketKassaMexaric.objects.all()
    serializer_class = ShirketKassaMexaricSerializer

# ********************************** Ofis kassa medaxil, mexaric put delete post get **********************************

class OfisKassaMedaxilListCreateAPIView(generics.ListCreateAPIView):
    queryset = OfisKassaMedaxil.objects.all()
    serializer_class = OfisKassaMedaxilSerializer

    def create(self, request, *args, **kwargs):
        return medaxil_mexaric_utils.ofis_kassa_medaxil_create(self, request, *args, **kwargs)


class OfisKassaMedaxilDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfisKassaMedaxil.objects.all()
    serializer_class = OfisKassaMedaxilSerializer

# **********************************

class OfisKassaMexaricListCreateAPIView(generics.ListCreateAPIView):
    queryset = OfisKassaMexaric.objects.all()
    serializer_class = OfisKassaMexaricSerializer

    def create(self, request, *args, **kwargs):
        return medaxil_mexaric_utils.ofis_kassa_mexaric_create(self, request, *args, **kwargs)


class OfisKassaMexaricDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfisKassaMexaric.objects.all()
    serializer_class = OfisKassaMexaricSerializer