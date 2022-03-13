from django.contrib.auth import user_logged_in
from rest_framework import status, permissions, generics
from rest_framework.exceptions import ValidationError

import math
import pandas as pd

import datetime
from dateutil.relativedelta import relativedelta

from rest_framework.response import Response
from rest_framework import generics
from .serializers import (
    AnbarSerializer,
    BolgeSerializer,
    HoldingSerializer,
    KomandaSerializer,
    EmeliyyatSerializer,
    OdemeTarixSerializer,
    MuqavileHediyyeSerializer,
    MehsullarSerializer,
    OfisSerializer,
    MuqavileSerializer,
    MusteriQeydlerSerializer,
    ShirketSerializer,
    ShobeSerializer,
    UserSerializer,
    MusteriSerializer,
    VezifelerSerializer,
    AnbarQeydlerSerializer,
    RegisterSerializer,
    ServisSerializer,
    StokSerializer,
    HoldingdenShirketlereTransferSerializer,
    ShirketdenHoldingeTransferSerializer,
    OfisdenShirketeTransferSerializer,
    ShirketdenOfislereTransferSerializer,
    OfisKassaSerializer,
    ShirketKassaSerializer,
    HoldingKassaSerializer,
    MaasSerializer,
    BonusSerializer,
)
from mehsullar.models import (
    Emeliyyat, 
    MuqavileHediyye, 
    Muqavile, 
    OdemeTarix, 
    Anbar, 
    Mehsullar, 
    AnbarQeydler, 
    Servis, 
    Stok
)
from account.models import (
    Bolge,
    MusteriQeydler, 
    Shirket, 
    Shobe, 
    User, 
    Musteri, 
    Vezifeler, 
    Ofis, 
    Komanda, 
    Holding, 
    ShirketKassa, 
    OfisKassa,
    HoldingKassa,
    HoldingdenShirketlereTransfer,
    OfisdenShirketeTransfer,
    ShirketdenHoldingeTransfer,
    ShirketdenOfislereTransfer,
    Maas,
    Bonus,
)
from rest_framework_simplejwt.views import TokenObtainPairView
from .utils.utils import jwt_decode_handler
from .utils import (
    odeme_tarixleri_utils,
    muqavile_utils,
    muqavile_hediyye_utils,
    anbar_emeliyyat_utils
)

from django_filters.rest_framework import DjangoFilterBackend

from .filters import (
    OdemeTarixFilter,
    MuqavileFilter,
    StokFilter,
)

from rest_framework.generics import get_object_or_404



# ********************************** user get post put delete **********************************


class RegisterApi(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Login(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        data = super().post(request, *args, **kwargs)

        data = data.data

        acces_token = jwt_decode_handler(data.get("access"))

        if not User.objects.filter(id=acces_token.get("user_id")).last():
            return Response({"error": True, "message": "No such a user"}, status=status.HTTP_404_NOT_FOUND)

        user = User.objects.filter(id=acces_token.get("user_id")).last()
        user_logged_in.send(sender=type(user), request=request, user=user)

        user_details = UserSerializer(user)

        data["user_details"] = user_details.data
        return Response(data)


# ********************************** musteri get post put delete **********************************
class MusteriListCreateAPIView(generics.ListCreateAPIView):
    queryset = Musteri.objects.all()
    serializer_class = MusteriSerializer


class MusteriDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Musteri.objects.all()
    serializer_class = MusteriSerializer


# ********************************** musteriqeydlerin put delete post get **********************************

class MusteriQeydlerListCreateAPIView(generics.ListCreateAPIView):
    queryset = MusteriQeydler.objects.all()
    serializer_class = MusteriQeydlerSerializer


class MusteriQeydlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MusteriQeydler.objects.all()
    serializer_class = MusteriQeydlerSerializer


# ********************************** muqavile get post put delete **********************************


class MuqavileListCreateAPIView(generics.ListCreateAPIView):
    queryset = Muqavile.objects.all()
    serializer_class = MuqavileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MuqavileFilter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        return muqavile_utils.muqavile_create(self, request, *args, **kwargs)


class MuqavileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Muqavile.objects.all()
    serializer_class = MuqavileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MuqavileFilter

    def patch(self, request, *args, **kwargs):
        return muqavile_utils.muqavile_patch(self, request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return muqavile_utils.muqavile_update(self, request, *args, **kwargs)

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

# ********************************** odeme tarixi put get post delete **********************************


class OdemeTarixListCreateAPIView(generics.ListCreateAPIView):
    queryset = OdemeTarix.objects.all()
    serializer_class = OdemeTarixSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OdemeTarixFilter

class OdemeTarixDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OdemeTarix.objects.all()
    serializer_class = OdemeTarixSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['muqavile']
    filterset_class = OdemeTarixFilter


    # PATCH SORGUSU
    def patch(self, request, *args, **kwargs):
        return odeme_tarixleri_utils.odeme_tarixi_patch(self, request, *args, **kwargs)

    # PUT SORGUSU
    def update(self, request, *args, **kwargs):
        return odeme_tarixleri_utils.odeme_tarixi_update(self, request, *args, **kwargs)


# ********************************** anbar put get post delete **********************************


class AnbarListCreateAPIView(generics.ListCreateAPIView):
    queryset = Anbar.objects.all()
    serializer_class = AnbarSerializer


class AnbarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anbar.objects.all()
    serializer_class = AnbarSerializer


# ********************************** mehsullar put get post delete **********************************


class MehsullarListCreateAPIView(generics.ListCreateAPIView):
    queryset = Mehsullar.objects.all()
    serializer_class = MehsullarSerializer


class MehsullarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mehsullar.objects.all()
    serializer_class = MehsullarSerializer


# ********************************** merkezler put delete post get **********************************


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


# ********************************** anbar put delete post get **********************************


class AnbarQeydlerListCreateAPIView(generics.ListCreateAPIView):
    queryset = AnbarQeydler.objects.all()
    serializer_class = AnbarQeydlerSerializer


class AnbarQeydlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnbarQeydler.objects.all()
    serializer_class = AnbarQeydlerSerializer


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


# ********************************** emeliyyat put delete post get **********************************


class EmeliyyatListCreateAPIView(generics.ListCreateAPIView):
    queryset = Emeliyyat.objects.all()
    serializer_class = EmeliyyatSerializer

    def create(self, request, *args, **kwargs):
        return anbar_emeliyyat_utils.emeliyyat_create(self, request, *args, **kwargs)

class EmeliyyatDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emeliyyat.objects.all()
    serializer_class = EmeliyyatSerializer


# ********************************** hediyye put delete post get **********************************


class MuqavileHediyyeListCreateAPIView(generics.ListCreateAPIView):
    queryset = MuqavileHediyye.objects.all()
    serializer_class = MuqavileHediyyeSerializer

    def create(self, request, *args, **kwargs):
        return muqavile_hediyye_utils.muqavile_hediyye_create(self, request, *args, **kwargs)


class MuqavileHediyyeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MuqavileHediyye.objects.all()
    serializer_class = MuqavileHediyyeSerializer


# ********************************** servis put delete post get **********************************

class ServisListCreateAPIView(generics.ListCreateAPIView):
    queryset = Servis.objects.all()
    serializer_class = ServisSerializer

    def perform_create(self, serializer):
        month6 = datetime.datetime.now() + datetime.timedelta(days=180)
        month18 = datetime.datetime.now() + datetime.timedelta(days=540)
        month24 = datetime.datetime.now() + datetime.timedelta(days=720)

        serializer.save(
            servis_tarix6ay=f"{month6.year}-{month6.month}-{datetime.datetime.now().day}",
            servis_tarix18ay=f"{month18.year}-{month18.month}-{datetime.datetime.now().day}",
            servis_tarix24ay=f"{month24.year}-{month24.month}-{datetime.datetime.now().day}"
        )


class ServisDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servis.objects.all()
    serializer_class = ServisSerializer


    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # indi_u = f"{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day}"
        indi = datetime.date.today()
        servis_tarix6ay = request.POST["servis_tarix6ay"]
        servis_tarix18ay = request.POST["servis_tarix18ay"]
        servis_tarix24ay = request.POST["servis_tarix24ay"]
        kartric1_id = int(request.POST["kartric1_id"])
        kartric2_id = int(request.POST["kartric2_id"])
        kartric3_id = int(request.POST["kartric3_id"])
        kartric4_id = int(request.POST["kartric4_id"])
        kartric5_id = int(request.POST["kartric5_id"])
        kartric6_id = int(request.POST["kartric6_id"])
        muqavile_id = request.POST["muqavile_id"]

        month6 = datetime.date.today() + datetime.timedelta(days=180)
        month18 = datetime.date.today() + datetime.timedelta(days=540)
        month24 = datetime.date.today() + datetime.timedelta(days=720)

        print(f"month6 ==> {month6}")
        print(f"month18 ==> {month18}")
        print(f"month24 ==> {month24}")
        print(f"{month6.year}-{month6.month}-{datetime.datetime.now().day}")

        print(f"indi --> {indi}")

        print(f"Tarix 6ay ==> {servis_tarix6ay}")
        print(f"Tarix 18ay ==> {servis_tarix18ay}")
        print(f"Tarix 24ay ==> {servis_tarix24ay}")

        print(f"kartric1_id ==> {kartric1_id}")
        print(f"kartric2_id ==> {kartric2_id}")
        print(f"kartric3_id ==> {kartric3_id}")
        print(f"kartric4_id ==> {kartric4_id}")
        print(f"kartric5_id ==> {kartric5_id}")
        print(f"kartric6_id ==> {kartric6_id}")

        try:
            muqavile = get_object_or_404(Muqavile, pk=muqavile_id)
            servis = get_object_or_404(Servis, muqavile=muqavile)
            print(servis)
            print(servis.servis_tarix6ay)
            print(type(servis.servis_tarix6ay))
            print(f"Muqavile ==> {muqavile}")
            print(f"Muqavile ofis ==> {muqavile.vanleader.ofis}")
            anbar = get_object_or_404(Anbar, ofis=muqavile.vanleader.ofis)
            print(f"Muqavile anbar ==> {anbar}")

            if (str(indi) != str(servis.servis_tarix6ay) and indi != str(servis.servis_tarix18ay) and indi != str(servis.servis_tarix24ay)):
                return Response({"Servis müddətinə hələ var"}, status=status.HTTP_404_NOT_FOUND)

            if (str(servis.servis_tarix6ay) == str(indi)):
                print(f"servis_tarix6ay == indi ===> {servis_tarix6ay == str(indi)}")
                try:
                    mehsul_kartric1 = get_object_or_404(Mehsullar, pk=kartric1_id)
                    mehsul_kartric2 = get_object_or_404(Mehsullar, pk=kartric2_id)
                    mehsul_kartric3 = get_object_or_404(Mehsullar, pk=kartric3_id)
                    mehsul_kartric4 = get_object_or_404(Mehsullar, pk=kartric4_id)

                    print(f"mehsul_kartric1 ==> {mehsul_kartric1}")
                    print(f"mehsul_kartric2 ==> {mehsul_kartric2}")
                    print(f"mehsul_kartric3 ==> {mehsul_kartric3}")
                    print(f"mehsul_kartric4 ==> {mehsul_kartric4}")

                    print(f"servis_tarix6ay ==> {servis_tarix6ay}")
                    try:
                        stok1 = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul_kartric1)
                        stok2 = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul_kartric2)
                        stok3 = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul_kartric3)
                        stok4 = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul_kartric4)

                        print(f"Muqavile stok1 ==> {stok1}")
                        print(f"Muqavile stok2 ==> {stok2}")
                        print(f"Muqavile stok3 ==> {stok3}")
                        print(f"Muqavile stok4 ==> {stok4}")
                        print(serializer.is_valid())

                        stok1.say = stok1.say - 1
                        stok2.say = stok2.say - 1
                        stok3.say = stok3.say - 1
                        stok4.say = stok4.say - 1
                        stok1.save()
                        stok2.save()
                        stok3.save()
                        stok4.save()
                        if (stok1.say == 0):
                            stok1.delete()

                        if (stok2.say == 0):
                            stok2.delete()

                        if (stok3.say == 0):
                            stok3.delete()

                        if (stok4.say == 0):
                            stok4.delete()
                        muqavile.servis.update(servis_tarix6ay=f"{month6.year}-{month6.month}-{datetime.date.today().day}")
                        super(ServisDetailAPIView, self).update(request, *args, **kwargs)
                        return Response({"Servis müvəffəqiyyətlə yeniləndi"}, status=status.HTTP_200_OK)
                    except:
                        return Response({"Anbarın stokunda məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)
                except:
                    return Response({"Bu adla məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)
            if (str(servis.servis_tarix18ay) == str(indi)):
                try:
                    mehsul_kartric5 = get_object_or_404(Mehsullar, pk=kartric5_id)

                    print(f"mehsul_kartric5 ==> {mehsul_kartric5}")
                    try:
                        stok5 = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul_kartric5)

                        print(f"Muqavile stok5 ==> {stok5}")

                        stok5.say = stok5.say - 1
                        stok5.save()

                        if (stok5.say == 0):
                            stok5.delete()

                        super(ServisDetailAPIView, self).update(request, *args, **kwargs)
                        return Response({"Servis müvəffəqiyyətlə yeniləndi"}, status=status.HTTP_200_OK)
                    except:
                        return Response({"Anbarın stokunda məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)
                except:
                    return Response({"Bu adla məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)
            if (str(servis.servis_tarix24ay) == str(indi)):
                try:
                    mehsul_kartric6 = get_object_or_404(Mehsullar, pk=kartric6_id)

                    print(f"mehsul_kartric6 ==> {mehsul_kartric6}")
                    try:
                        stok6 = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul_kartric6)

                        print(f"Muqavile stok6 ==> {stok6}")

                        stok6.say = stok6.say - 1
                        stok6.save()

                        if (stok6.say == 0):
                            stok6.delete()
                        super(ServisDetailAPIView, self).update(request, *args, **kwargs)
                        return Response({"Servis müvəffəqiyyətlə yeniləndi"}, status=status.HTTP_200_OK)
                    except:
                        return Response({"Anbarın stokunda məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)
                except:
                    return Response({"Bu adla məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"Belə bir müqavilə tapılmadı"}, status=status.HTTP_404_NOT_FOUND)

# ********************************** stok put delete post get **********************************

class StokListCreateAPIView(generics.ListCreateAPIView):
    queryset = Stok.objects.all()
    serializer_class = StokSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StokFilter


class StokDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stok.objects.all()
    serializer_class = StokSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StokFilter

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        mehsul_id = int(request.POST["mehsul_id"])
        say = int(request.POST["say"])
        anbar_id = int(request.POST["anbar_id"])
        print(f"mehsul id ==> {mehsul_id}")
        print(f"anbar id ==> {anbar_id}")
        print(f"say ==> {say}")

        mehsul = get_object_or_404(Mehsullar, pk = mehsul_id)
        print(f"Mehsul ==> {mehsul}")
        anbar = get_object_or_404(Anbar, pk=anbar_id)
        print(f"anbar ==> {anbar}")
        try:
            stok = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul)
            print(f"stok ==> {stok}")

            print(f"evvel mehsul_sayi ==> {stok.say}")
            stok.say = stok.say + say
            print(f"sonra mehsul_sayi ==> {stok.say}")
            print("1 ishe dushdu ***********")
            stok.save()
            # super(StokSerializer, self).update(request, *args, **kwargs)
            print("2 ishe dushdu ***********")
            return Response({f"Anbardakı {mehsul} adlı məhsulun sayı artırıldı."}, status=status.HTTP_200_OK)
        except:
            print("3 ishe dushdu ***********")
            return Response({"Problem"}, status=status.HTTP_404_NOT_FOUND)


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

# ********************************** ishci maas put delete post get **********************************

class MaasListCreateAPIView(generics.ListCreateAPIView):
    queryset = Maas.objects.all()
    serializer_class = MaasSerializer

class MaasDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Maas.objects.all()
    serializer_class = MaasSerializer

# ********************************** ishci elave bonus put delete post get **********************************

class BonusListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer

class BonusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer

# ********************************** bolge put delete post get **********************************

class BolgeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bolge.objects.all()
    serializer_class = BolgeSerializer


class BolgeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bolge.objects.all()
    serializer_class = BolgeSerializer