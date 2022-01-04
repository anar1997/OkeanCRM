from django.db.models import query
from django.db.models.query import QuerySet
from rest_framework import generics, serializers
from  .serializers import AnbarSerializer, EmeliyyatSerializer, DatesSerializer, MehsullarSerializer, MerkezlerSerializer, MuqavileSerializer, MusteriQeydlerSerializer, ShirketSerializer, ShobeSerializer, UserSerializer, MusteriSerializer, VezifelerSerializer, AnbarQeydlerSerializer
from mehsullar.models import Emeliyyat, Muqavile, Dates, Anbar, Mehsullar, AnbarQeydler
from account.models import MusteriQeydler, Shirket, Shobe, User, Musteri,  Vezifeler, Merkezler

# user get post put delete
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializers_class=UserSerializer


# musteri get post put delete
class MusteriListCreateAPIView(generics.ListCreateAPIView):
    queryset=Musteri.objects.all()
    serializer_class=MusteriSerializer
class MusteriDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Musteri.objects.all()
    serializer_class=MusteriSerializer

# muqavile get post put delete

class MuqavileListCreateAPIView(generics.ListCreateAPIView):
    queryset=Muqavile.objects.all()
    serializer_class=MuqavileSerializer
class MuqavileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Muqavile.objects.all()
    serializer_class=MuqavileSerializer

# date put get post delete

class DatesListCreateAPIView(generics.ListCreateAPIView):
    queryset=Dates.objects.all()
    serializer_class=DatesSerializer
class DatesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Dates.objects.all()
    serializer_class=DatesSerializer

# anbar put get post delete

class AnbarListCreateAPIView(generics.ListCreateAPIView):
    queryset=Anbar.objects.all()
    serializer_class=AnbarSerializer
class AnbarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Anbar.objects.all()
    serializer_class=AnbarSerializer

#  mehsullar put get post delete

class MehsullarListCreateAPIView(generics.ListCreateAPIView):
    queryset=Mehsullar.objects.all()
    serializer_class=MehsullarSerializer
class MehsullarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Mehsullar.objects.all()
    serializer_class=MehsullarSerializer
#  kateqoriyalar put delete post get

# class KateqoriyalarListCreateAPIView(generics.ListCreateAPIView):
#     queryset=Kateqoriyalar.objects.all()
#     serializer_class=KateqoriyalarSerializer
# class KateqoriyalarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Kateqoriyalar.objects.all()
#     serializer_class=KateqoriyalarSerializer

#  merkezler put delete post get
class MerkezlerListCreateAPIView(generics.ListCreateAPIView):
    queryset=Merkezler.objects.all()
    serializer_class=MerkezlerSerializer

class MerkezlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Merkezler.objects.all()
    serializer_class=MerkezlerSerializer
#  vezifeler put delete post get
class VezifelerListCreateAPIView(generics.ListCreateAPIView):
    queryset=Vezifeler.objects.all()
    serializer_class=VezifelerSerializer
class VezifelerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Vezifeler.objects.all()
    serializer_class=VezifelerSerializer

class AnbarQeydlerListCreateAPIView(generics.ListCreateAPIView):
    queryset=AnbarQeydler.objects.all()
    serializer_class=AnbarQeydlerSerializer
class AnbarQeydlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=AnbarQeydler.objects.all()
    serializer_class=AnbarQeydlerSerializer

# musteriqeydlerin put delete post get

class MusteriQeydlerListCreateAPIView(generics.ListCreateAPIView):
    queryset=MusteriQeydler.objects.all()
    serializer_class=MusteriQeydlerSerializer
class MusteriQeydlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=MusteriQeydler.objects.all()
    serializer_class=MusteriQeydlerSerializer

# shirket put delete post get

class ShirketListCreateAPIView(generics.ListCreateAPIView):
    queryset=Shirket.objects.all()
    serializer_class=ShirketSerializer
class ShirketDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Shirket.objects.all()
    serializer_class=ShirketSerializer

# shobe put delete post get

class ShobeListCreateAPIView(generics.ListCreateAPIView):
    queryset=Shobe.objects.all()
    serializer_class=ShobeSerializer

class ShobeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Shobe.objects.all()
    serializer_class=ShobeSerializer

# emeliyyat put delete post get

class EmeliyyatListCreateAPIView(generics.ListCreateAPIView):
    queryset=Emeliyyat.objects.all()
    serializer_class=EmeliyyatSerializer
class EmeliyyatDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Emeliyyat.objects.all()
    serializer_class=EmeliyyatSerializer