from rest_framework import generics
from django.contrib.auth import user_logged_in
from rest_framework import status
from rest_framework.exceptions import ValidationError

from rest_framework.response import Response
from rest_framework import generics
from .serializers import (
    AnbarSerializer,
    KomandaSerializer,
    EmeliyyatSerializer,
    DatesSerializer,
    HediyyeSerializer,
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
)
from mehsullar.models import Emeliyyat, Hediyye, Muqavile, Dates, Anbar, Mehsullar, AnbarQeydler, Servis, Stok
from account.models import MusteriQeydler, Shirket, Shobe, User, Musteri,  Vezifeler, Ofis, Komanda
from rest_framework_simplejwt.views import TokenObtainPairView
from .utils import jwt_decode_handler

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin

from django_filters.rest_framework import DjangoFilterBackend

from .filters import (
    DatesFilter,
    MuqavileFilter,
)

import datetime
from rest_framework.views import APIView
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        user = self.request.user
        print(f"login olan user ==> {user}")

        mehsul_id = int(request.POST["mehsul_id"])
        print(f"mehsul id ==> {mehsul_id}")
        mehsul = get_object_or_404(Mehsullar, pk=mehsul_id)
        print(f"mehsul ==> {mehsul}")


        if(user.is_superuser == True or user.vezife.vezife_adi == "VANLEADER"):
            anbar = get_object_or_404(Anbar, ofis=user.ofis)
            print(f"anbar ==> {anbar}")
            print(f"ofis ==> {user.ofis}")

            try:
                stok = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul)
                print(f"stok ==> {stok}")
                if(serializer.is_valid()):
                    serializer.save(vanleader=user)
                    stok.say = stok.say-1
                    if(stok.say==0):
                        stok.delete()
                    stok.save()
                    return Response({"Müqavilə müvəffəqiyyətlə imzalandı"}, status=status.HTTP_201_CREATED)
            except:
                return Response({"Anbarın stokunda məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)

class MuqavileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Muqavile.objects.all()
    serializer_class = MuqavileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MuqavileFilter

# ********************************** komanda get post put delete **********************************


class KomandaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Komanda.objects.all()
    serializer_class = KomandaSerializer


class KomandaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Komanda.objects.all()
    serializer_class = KomandaSerializer


# ********************************** date put get post delete **********************************


class DatesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Dates.objects.all()
    serializer_class = DatesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DatesFilter


class DatesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dates.objects.all()
    serializer_class = DatesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['muqavile']
    filterset_class = DatesFilter

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
        serializer = self.get_serializer(data=request.data)
        gonderen = int(request.POST["gonderen_id"])
        # print(f"Gonderen id ==> {gonderen}")
        gonderen_anbar = get_object_or_404(Anbar, pk=gonderen)
        # print(f"Gonderen anbar ==> {gonderen_anbar}")
        qebul_eden_id = int(request.POST["qebul_eden_id"])
        # print(f"qebul_eden id ==> {qebul_eden_id}")
        qebul_eden = get_object_or_404(Anbar, pk=qebul_eden_id)
        # print(f"qebul_eden anbar ==> {qebul_eden}")

        gonderilen_mehsul_id = int(request.POST["gonderilen_mehsul_id"])
        # print(f"Gonderilen mehsul id ==> {gonderilen_mehsul_id}")
        gonderilen_mehsul = get_object_or_404(Mehsullar, pk=gonderilen_mehsul_id)
        # print(f"Gonderilen mehsul ==> {gonderilen_mehsul}")
        say = int(request.POST["mehsulun_sayi"])
        # print(f"say ==> {say}")

        qeyd = request.POST["qeyd"]
        print(f"qeyd ==> {qeyd}")

        try:
            stok1 = get_object_or_404(Stok, anbar=gonderen_anbar, mehsul=gonderilen_mehsul)
            stok2 = get_object_or_404(Stok, anbar=qebul_eden)
            if (stok1 == stok2):
                # print("BURA ISE DUSDU")
                return Response({"Göndərən və göndərilən anbar eynidir!"}, status=status.HTTP_404_NOT_FOUND)
            # print(f"Stok1 ==> {stok1}")
            # print(f"stok1.say ==> {stok1.say}")
            if (say > stok1.say):
                return Response({"Göndərən anbarda yetəri qədər məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)
            stok1.say = stok1.say - say
            # print(f"stok1.say ==> {stok1.say}")
            stok1.save()
            # print("1 calisdi **********")
            if (stok1.say == 0):
                stok1.delete()
                # print(f"stok1.say ==> {stok1.say}")
                # print("2 calisdi **********")
            try:
                # print(f"stok2 ==> {stok2}")
                # print(f"stok2.say ==> {stok2.say}")
                stok2.say = stok2.say + say
                stok2.save()
                # print(f"stok2.say ==> {stok2.say}")
                # print("3 calisdi **********")
                if (serializer.is_valid()):
                    serializer.save(gonderen=gonderen_anbar)
                return Response({"Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
            except:
                stok2 = Stok.objects.create(anbar=qebul_eden, mehsul=gonderilen_mehsul, say=say)
                if (stok1 == stok2):
                    # print("BURA DAAAA ISE DUSDU")
                    return Response({"Göndərən və göndərilən anbar eynidir!"}, status=status.HTTP_404_NOT_FOUND)
                stok2.save()
                # print(f"stok2.say ==> {stok2.say}")
                # print("4 calisdi **********")
                if (serializer.is_valid()):
                    serializer.save(gonderen=gonderen_anbar)
                return Response({"Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
        except:
            # print("5 calisdi **********")
            return Response({"Göndərən anbarda məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)


class EmeliyyatDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emeliyyat.objects.all()
    serializer_class = EmeliyyatSerializer

# ********************************** hediyye put delete post get **********************************


class HediyyeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Hediyye.objects.all()
    serializer_class = HediyyeSerializer


class HediyyeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hediyye.objects.all()
    serializer_class = HediyyeSerializer

# ********************************** servis put delete post get **********************************

class ServisListCreateAPIView(generics.ListCreateAPIView):
    queryset = Servis.objects.all()
    serializer_class = ServisSerializer

    def perform_create(self, serializer): 
        month6 = datetime.datetime.now() + datetime.timedelta(days=180)
        month18 = datetime.datetime.now() + datetime.timedelta(days=540)
        month24 = datetime.datetime.now() + datetime.timedelta(days=720)

        serializer.save(
            servis_tarix6ay = f"{month6.year}-{month6.month}-{datetime.datetime.now().day}",
            servis_tarix18ay = f"{month18.year}-{month18.month}-{datetime.datetime.now().day}",
            servis_tarix24ay = f"{month24.year}-{month24.month}-{datetime.datetime.now().day}"
        )

class ServisDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servis.objects.all()
    serializer_class = ServisSerializer

    def perform_update(self, serializer):
        indi = f"{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day}"
        month6 = datetime.datetime.now() + datetime.timedelta(days=180)
        month18 = datetime.datetime.now() + datetime.timedelta(days=540)
        month24 = datetime.datetime.now() + datetime.timedelta(days=720)
        print(f'tarix --> {serializer.validated_data.get("servis_tarix6ay")}')
        print(f"indi --> {indi}")
        if(serializer.validated_data.get("servis_tarix6ay").__eq__(indi)):
            serializer.save(servis_tarix6ay = f"{month6.year}-{month6.month}-{datetime.datetime.now().day}")

        if(serializer.validated_data.get("servis_tarix18ay").__eq__(indi)):
            serializer.save(servis_tarix18ay = f"{month18.year}-{month18.month}-{datetime.datetime.now().day}")

        if(serializer.validated_data.get("servis_tarix24ay").__eq__(indi)):
            serializer.save(servis_tarix24ay = f"{month24.year}-{month24.month}-{datetime.datetime.now().day}")

# ********************************** stok put delete post get **********************************

class StokListCreateAPIView(generics.ListCreateAPIView):
    queryset = Stok.objects.all()
    serializer_class = StokSerializer

class StokDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stok.objects.all()
    serializer_class = StokSerializer
