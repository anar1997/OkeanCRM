from django.db.models.query import QuerySet
from rest_framework import generics, serializers
from  .serializers import AnbarSerializer, KateqoriyalarSerializer, DatesSerializer, MehsullarSerializer, MuqavileSerializer, UserSerializer, MusteriSerializer
from mehsullar.models import Muqavile, Dates, Anbar, Kateqoriyalar, Mehsullar
from account.models import User, Musteri, UserVezifeler, Vezifeler
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
    seializer_class=AnbarSerializer
class AnbarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Anbar.objects.all()
    seializer_class=AnbarSerializer

#  mehsullar put get post delete

class MehsullarListCreateAPIView(generics.ListCreateAPIView):
    queryset=Mehsullar.objects.all()
    serializer_class=MehsullarSerializer
class MehsullarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Mehsullar.objects.all()
    serializer_class=MehsullarSerializer
#  kateqoriyalar put delete post get

class KateqoriyalarListCreateAPIView(generics.ListCreateAPIView):
    queryset=Kateqoriyalar.objects.all()
    serializer_class=KateqoriyalarSerializer
class KateqoriyalarDetailAPIView(generics.ListCreateAPIView):
    queryset=Kateqoriyalar.objects.all()
    serializer_class=KateqoriyalarSerializer