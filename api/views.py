from rest_framework import generics
from django.contrib.auth import user_logged_in
from rest_framework import status

from rest_framework.response import Response
from rest_framework import generics
from .serializers import (
    AnbarSerializer,
    KomandaSerializer,
    EmeliyyatSerializer,
    DatesSerializer,
    HediyyeSerializer,
    MehsullarSerializer,
    MerkezlerSerializer,
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
from account.models import MusteriQeydler, Shirket, Shobe, User, Musteri,  Vezifeler, Merkezler, Komanda
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
        vanleader = self.request.user
        user = get_object_or_404(User, pk=vanleader.id)
        anbar = get_object_or_404(Anbar, merkez=user.ofis)
        stok = get_object_or_404(Stok, anbar=anbar, mehsul=serializer.is_valid("mehsul"))

        serializer.save(vanleader=user)
        stok.say = stok.say-1
        
        if(stok.say==0):
            stok.delete()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        stok.save()

        if(stok==None):
            return Response({"detail":"Stokda məhsul yoxdur!"}, serializer.data, status=status.HTTP_404_NOT_FOUND)
        
        stok.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
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


class MerkezlerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Merkezler.objects.all()
    serializer_class = MerkezlerSerializer


class MerkezlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Merkezler.objects.all()
    serializer_class = MerkezlerSerializer
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
